package cmd

import (
	"fmt"
	"os"
	"path/filepath"
	"text/template"

	"github.com/spf13/cobra"
)

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "get-template",
	Short: "Tool to interact with file templates.",
	Long: `get-template is a CLI tool that helps to speed up development.
	It does this by giving you a selction of templates to choose from.`,
}

var tmpl *template.Template

func init() {
	dir, exists := os.LookupEnv("TEMPLATE_DIRECTORY")
	if !exists {
		fmt.Println("TEMPLATE_DIRECTORY not set")
		os.Exit(1)
	}

	pattern := filepath.Join(dir, "*")
	tmpl = template.Must(template.ParseGlob(pattern))
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
