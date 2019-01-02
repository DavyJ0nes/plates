package cmd

import (
	"fmt"
	"github.com/pkg/errors"
	"github.com/spf13/cobra"
	"os"
	"os/exec"
	"path/filepath"
)

// initCmd represents the init command
var initCmd = &cobra.Command{
	Use:   "init",
	Short: "initialises go project in current directory",
	Long: `Example
	plates init`,
	Run: func(cmd *cobra.Command, args []string) {
		if args[0] == "help" {
			cmd.Help()
			os.Exit(1)
		}
		if err := initCommand(); err != nil {
			fmt.Printf("Error initialing:\n %v\n", err)
			os.Exit(1)
		}
	},
}

func init() {
	rootCmd.AddCommand(initCmd)
}

func initCommand() error {
	// check if dir has .git
	currDir, _ := os.Getwd()
	gitPath := filepath.Join(currDir, ".git")
	err := os.Chdir(gitPath)
	if err != nil {
		if os.IsExist(err) {
			return errors.New("directory already initialised")
		}
		return err
	}

	// mkdir cmd/
	cmdPath := filepath.Join(currDir, "cmd")
	err = os.Mkdir(cmdPath, os.ModeDir)
	if err != nil {
		return err
	}

	fileMap := map[string]string{
		"gitignore-go": ".gitignore",
		"Makefile-go":  "Makefile",
		"README.md":    "README.md",
		"main.go":      "cmd/main.go",
		"main_test.go": "cmd/main_test.go",
	}

	for src, dest := range fileMap {
		err = copyCommand([]string{src, dest})
		if err != nil {
			return err
		}
	}

	initCmds := []string{"dep", "git"}
	for _, cmdName := range initCmds {
		cmd := exec.Command(cmdName, "init")
		err = cmd.Run()
		if err != nil {
			return err
		}
	}

	return nil
}
