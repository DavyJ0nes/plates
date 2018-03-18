package cmd

import (
	"fmt"
	"os"
	"path/filepath"
	"text/template"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"
)

// copyCmd represents the copy command
var copyCmd = &cobra.Command{
	Use:   "copy",
	Short: "Copies a template to the current directory",
	Long: `Example
	get-template copy <src_template> <dest_name>`,
	Run: func(cmd *cobra.Command, args []string) {
		if args[0] == "help" {
			cmd.Help()
			os.Exit(1)
		}
		if err := copyCommand(args); err != nil {
			fmt.Printf("Error Copying Template:\n %v\n", err)
			os.Exit(1)
		}
	},
}

func init() {
	rootCmd.AddCommand(copyCmd)
	// copyCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

func copyCommand(args []string) error {
	src := args[0]
	dest := args[1]
	srcTmpl, err := findTemplate(src)
	if err != nil {
		return errors.Wrap(err, "Error Finding Template")
	}

	currDir, _ := os.Getwd()
	destPath := filepath.Join(currDir, dest)

	err = copyTemplate(srcTmpl, destPath)
	if err != nil {
		return errors.Wrap(err, "Error Copying Template")
	}

	return nil
}

func findTemplate(name string) (*template.Template, error) {
	var template *template.Template
	for _, plate := range tmpl.Templates() {
		if plate.Name() == name {
			template = plate
			return template, nil
		}
	}
	return template, errors.Errorf("Couldn't Find Template: %s", name)

}

func copyTemplate(src *template.Template, dest string) error {
	fmt.Printf("Copying %s to %s\n", src.Name(), dest)
	destFile, err := os.Create(dest)
	if err != nil {
		return errors.Wrap(err, "Error Creating Destination File")
	}
	defer destFile.Close()

	err = src.Execute(destFile, nil)
	if err != nil {
		return errors.Wrap(err, "Error Executing Template")
	}

	return nil
}
