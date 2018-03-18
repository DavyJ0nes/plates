all: build

# Makefile for file-templates tool

# To build the binary for your OS run:
# $ make

#### VARIABLES ####
APP_NAME = file-templates
PROJECT ?= github.com/davyj0nes/file-templates

RELEASE = 0.1.0
COMMIT = $(shell git rev-parse HEAD | cut -c 1-6)
BUILD_TIME = $(shell date -u '+%Y-%m-%d_%I:%M:%S%p')

GO_OS = $(shell uname | tr '[:upper:]' '[:lower:]')
USER_BIN_DIR = $(HOME)/bin

LDFLAGS = -ldflags "-s -w -X ${PROJECT}/cmd.Release=${RELEASE} -X ${PROJECT}/cmd.Commit=${COMMIT} -X ${PROJECT}/cmd.BuildTime=${BUILD_TIME}"

GO_VERSION ?= 1.10

.PHONY: run build install test clean

#### COMMANDS ####
run:
	$(call blue, "# Running App...")
	@docker run -it --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} go run main.go

build:
	$(call blue, "# Building Golang Binary...")
	@docker run --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} sh -c 'go get && GOOS=${GO_OS} go build ${LDFLAGS} -o ${APP_NAME}'

install: build
	$(call blue, "# Installing Binary...")
	@cp ${APP_NAME} ${USER_BIN_DIR}/${APP_NAME}
	@$(MAKE) clean

test:
	$(call blue, "# Testing Golang Code...")
	@docker run --rm -it -v "$(GOPATH):/go" -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} sh -c 'go test -v' 

clean: 
	@rm -f ${app_name} 

#### FUNCTIONS ####
define blue
	@tput setaf 4
	@echo $1
	@tput sgr0
endef