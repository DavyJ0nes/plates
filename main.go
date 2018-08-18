//go:generate fileb0x generate-templates.yaml
package main

import "github.com/davyj0nes/plates/cmd"

func main() {
	cmd.Execute()
}
