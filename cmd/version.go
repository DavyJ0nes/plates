package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(versionCmd)
}

var (
	// BuildTime is a time label from when the binary was built.
	BuildTime = "unset"
	// Commit is the git hash from when the binary was built
	Commit = "unset"
	// Release is the semantic version of the current build
	Release = "unset"
)

// versionCmd represents the version command
var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "output version information",
	Run: func(cmd *cobra.Command, args []string) {
		printVersion()
	},
}

func printVersion() {
	fmt.Printf("version: %s (%s, %s)\n", Release, Commit, BuildTime)
}
