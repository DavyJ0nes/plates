package cmd

import (
	"fmt"
	"os"
	"text/template"

	"github.com/davyj0nes/file-templates/static"

	"github.com/spf13/cobra"
)

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "file-templates",
	Short: "Tool to interact with file templates.",
	Long: `file-templates is a CLI tool that helps to speed up development.
	It does this by giving you a selction of templates to choose from and
	allows you to copy them into your local directory.`,
}

var tmpls []*template.Template

func init() {
	fileSlice, err := static.WalkDirs("", false)
	if err != nil {
		fmt.Println("Issue Walking Directories")
		os.Exit(1)
	}

	for _, file := range fileSlice {
		fileText, err := static.ReadFile(file)
		if err != nil {
			fmt.Println("Problem Reading File")
			os.Exit(1)
		}
		tmpls = append(tmpls, template.Must(template.New(file).Parse(string(fileText))))
	}
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
