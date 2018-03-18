all: build

# Makefile for file-templates tool

# To build the binary for your OS run:
# $ make

#### VARIABLES ####
APP_NAME = file-templates
GO_PROJECT_PATH ?= github.com/davyj0nes/file-templates

RELEASE = 0.2.0
COMMIT = $(shell git rev-parse HEAD | cut -c 1-6)
BUILD_TIME = $(shell date -u '+%Y-%m-%d_%I:%M:%S%p')

GO_OS = $(shell uname | tr '[:upper:]' '[:lower:]')
USER_BIN_DIR = $(HOME)/bin

BUILD_PREFIX = CGO_ENABLED=0 GOOS=linux
BUILD_FLAGS = -a -tags netgo --installsuffix netgo
LDFLAGS = -ldflags "-s -w -X ${GO_PROJECT_PATH}/cmd.Release=${RELEASE} -X ${GO_PROJECT_PATH}/cmd.Commit=${COMMIT} -X ${GO_PROJECT_PATH}/cmd.BuildTime=${BUILD_TIME}"
DOCKER_GO_BUILD = docker run --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION}
GO_BUILD_LINUX = $(BUILD_PREFIX) go build $(BUILD_FLAGS) $(LDFLAGS)
GO_BUILD_OSX = GOOS=darwin GOARCh=amd64 go build $(LDFLAGS)
GO_BUILD_WIN = GOOS=windows GOARCh=amd64 go build $(LDFLAGS)

GO_VERSION ?= 1.10

#### COMMANDS ####
.PHONY: run
run:
	$(call blue, "# Running App...")
	@docker run -it --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} go run main.go

.PHONY: generate
generate:
	$(call blue, "# Generating Static Templates...")
	@docker run --rm -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} go get -u github.com/UnnoTed/fileb0x && go generate

.PHONY: release
release: generate
	$(call blue, "# Creating New Release: ${RELEASE} ...")
	@mkdir -p releases/${RELEASE}
	$(call blue, "  # Compiling Linux Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_LINUX} -o releases/${RELEASE}/${APP_NAME}_linux'
	$(call blue, "  # Compiling OSX Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_OSX} -o releases/${RELEASE}/${APP_NAME}_osx'
	$(call blue, "  # Compiling Windows Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_WIN} -o releases/${RELEASE}/${APP_NAME}.exe'

.PHONY: build
build: generate
	$(call blue, "# Building Golang Binary...")
	@docker run --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} sh -c 'go get && GOOS=${GO_OS} go build ${LDFLAGS} -o ${APP_NAME}'

.PHONY: install
install: build
	$(call blue, "# Installing Binary...")
	@cp ${APP_NAME} ${USER_BIN_DIR}/${APP_NAME}
	@$(MAKE) clean

.PHONY: test
test:
	$(call blue, "# Testing Golang Code...")
	@docker run --rm -it -v "$(GOPATH):/go" -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} sh -c 'go test -v' 

.PHONY: clean
clean: 
	@rm -f ${APP_NAME} 

#### FUNCTIONS ####
define blue
	@tput setaf 4
	@echo $1
	@tput sgr0
endef
