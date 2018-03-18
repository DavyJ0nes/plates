#!/bin/bash
set -e

#==================================#
# Example Bash Script
# 2018
#==================================#
 
print_usage() {
 echo "usage: $1 <arg>"
 echo ""
 echo "Template Bash Script"
 echo " - arg: command line arguement for script"
}
 
# VARIABLES
arg=$1
 
# PRINT OUTPUT
echo "arg = $arg"