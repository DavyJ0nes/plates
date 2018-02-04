all: build

# Makefile for get-template tool

# To build the binary for your OS run:
# $ make

#### VARIABLES ####
app_name = get-template
binary_version = 0.0.1
go_os = $(shell uname | tr '[:upper:]' '[:lower:]')
user_bin_dir = $(HOME)/bin

go_version ?= 1.9.2

git_hash = $(shell git rev-parse HEAD | cut -c 1-6)
build_date = $(shell date -u '+%Y-%m-%d_%I:%M:%S%p')

.PHONY: run build install test clean

#### COMMANDS ####
run:
	$(call blue, "# Running App...")
	@docker run -it --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -p ${local_port}:${app_port} -w /go/src/app golang:${go_version} go run main.go

build:
	$(call blue, "# Building Golang Binary...")
	@docker run --rm -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${go_version} sh -c 'go get && GOOS=${go_os} go build -o ${app_name}'

install: build
	$(call blue, "# Installing Binary...")
	# @docker build --label APP_VERSION=${binary_version} --label BUILT_ON=${build_date} --label GIT_HASH=${git_hash} -t ${username}/${app_name}:${image_version} .
	@cp ${app_name} ${user_bin_dir}/${app_name}
	@$(MAKE) clean

test:
	$(call blue, "# Testing Golang Code...")
	@docker run --rm -it -v "$(GOPATH):/go" -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${go_version} sh -c 'go test -v' 

clean: 
	@rm -f ${app_name} 

#### FUNCTIONS ####
define blue
	@tput setaf 4
	@echo $1
	@tput sgr0
endef
