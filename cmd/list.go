package cmd

import (
	"fmt"
	"os"
	"strings"

	"github.com/spf13/cobra"
)

// listCmd represents the list command
var listCmd = &cobra.Command{
	Use:   "list",
	Short: "returns a list of available templates",
	Run: func(cmd *cobra.Command, args []string) {
		if err := listTemplates(); err != nil {
			fmt.Printf("Error Listing Templates:\n %v\n", err)
			os.Exit(1)
		}
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
}

func listTemplates() error {
	for id, plate := range tmpls {
		friendlyName := strings.Split(plate.Name(), "templates/")[1]
		fmt.Printf("%d.\t%s\n", id+1, friendlyName)
	}
	return nil
}
