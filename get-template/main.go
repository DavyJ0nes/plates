package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"strings"

	"github.com/pkg/errors"
)

var (
	templateDir string
	currentDir  string
)

func init() {
	templateDir = os.Getenv("TEMPLATE_DIR")
	if templateDir == "" {
		fmt.Println("TEMPLATE_DIR envar is not configured\nPlease set to the directory of the temlates")
		os.Exit(1)
	}

	var err error
	currentDir, err = os.Getwd()
	check(err)
}

func main() {
	list := flag.Bool("list", false, "List out the templates")
	file := flag.String("file", "", "The template file to copy")

	flag.Usage = func() {
		fmt.Println("get-template [options]")
		flag.PrintDefaults()
		os.Exit(1)
	}

	flag.Parse()

	if *list {
		templates, err := listTemplates()
		check(err)

		fmt.Println(templates)
		os.Exit(1)
	}

	if *file == "" {
		fmt.Println("No file specified")
		flag.Usage()
	}

	err := copyTemplate(*file)
	check(err)
}

// check is a refactoring that panics on errors
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// listTemplates prints the available tempaltes to stdout
func listTemplates() (string, error) {
	var listOfTemplates string
	files, err := ioutil.ReadDir(templateDir)

	if err != nil {
		return "", errors.Wrap(err, "listTemplates")
	}

	for _, file := range files {
		if strings.HasSuffix(file.Name(), ".example") {
			listOfTemplates = fmt.Sprintf("%s\n%s", listOfTemplates, file.Name())
		}
	}

	return strings.Trim(listOfTemplates, "\n"), nil
}

// copyTemplate copies the template file to the current directory
func copyTemplate(file string) error {
	sourceFileFullPath := fmt.Sprintf("%s/%s", templateDir, file)
	sourceFile, err := ioutil.ReadFile(sourceFileFullPath)
	if err != nil {
		return errors.Wrap(err, "copyTemplate")
	}

	splitFileName := strings.Split(file, ".")

	var trimmedFileName string
	if splitFileName[0] == "README" {
		trimmedFileName = "README.md"
	} else {
		trimmedFileName = splitFileName[0]
	}

	targetFileFullPath := fmt.Sprintf("%s/%s", currentDir, trimmedFileName)
	err = ioutil.WriteFile(targetFileFullPath, sourceFile, 0644)
	if err != nil {
		return errors.Wrap(err, "copyTemplate")
	}
	fmt.Printf("Created %s\n", trimmedFileName)

	return nil
}
