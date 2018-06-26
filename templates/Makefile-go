#### VARIABLES ####
USERNAME = davyj0nes
APP_NAME = app_name

GO_VERSION ?= 1.10.3
GO_PROJECT_PATH ?= github.com/davyj0nes/app_name
GO_FILES = $(shell go list ./... | grep -v /vendor/)

RELEASE = 0.0.1
COMMIT = $(shell git rev-parse HEAD | cut -c 1-6)
BUILD_TIME = $(shell date -u '+%Y-%m-%d_%I:%M:%S%p')

BUILD_PREFIX = CGO_ENABLED=0 GOOS=linux
BUILD_FLAGS = -a -tags netgo --installsuffix netgo
LDFLAGS = -ldflags "-s -w -X ${GO_PROJECT_PATH}/cmd.Release=${RELEASE} -X ${GO_PROJECT_PATH}/cmd.Commit=${COMMIT} -X ${GO_PROJECT_PATH}/cmd.BuildTime=${BUILD_TIME}"
DOCKER_GO_BUILD = docker run --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION}
GO_BUILD_STATIC = $(BUILD_PREFIX) go build $(BUILD_FLAGS) $(LDFLAGS)
GO_BUILD_OSX = GOOS=darwin GOARCh=amd64 go build $(LDFLAGS)
GO_BUILD_WIN = GOOS=windows GOARCh=amd64 go build $(LDFLAGS)

DOCKER_RUN_CMD = docker run -it --rm -v ${APP_NAME}:/app/.tasks --name ${APP_NAME} ${USERNAME}/${APP_NAME}:${IMAGE_VERSION} "\$$@"

#### COMMANDS ####
.PHONY: compile
compile:
	@mkdir -p releases/${RELEASE}
	$(call blue, "# Compiling Static Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_STATIC} -o ${APP_NAME}_static'
	$(call blue, "# Compiling OSX Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_OSX} -o releases/${RELEASE}/${APP_NAME}_osx'
	$(call blue, "# Compiling Windows Golang App...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_WIN} -o releases/${RELEASE}/${APP_NAME}.exe'

.PHONY: binary
binary:
	$(call blue, "# Building Golang Binary...")
	@${DOCKER_GO_BUILD} sh -c 'go get && ${GO_BUILD_STATIC} -o ${APP_NAME}_static'

.PHONY: image
image: binary
	$(call blue, "# Building Docker Image...")
	@docker build --no-cache --label APP_VERSION=${RELEASE} --label BUILT_ON=${BUILD_TIME} --label GIT_HASH=${COMMIT} -t ${USERNAME}/${APP_NAME}:${RELEASE} .
	@docker tag ${USERNAME}/${APP_NAME}:${RELEASE} ${USERNAME}/${APP_NAME}:latest
	@$(MAKE) clean

.PHONY: publish
publish: image
        $(call blue, "# Publishing Docker Image...")
        @docker push docker.io/${USERNAME}/${APP_NAME}:${RELEASE}

.PHONY: run
run:
	$(call blue, "# Running App...")
	@docker run -it --rm -v "$(GOPATH)":/go -v "$(CURDIR)":/go/src/app -p ${local_port}:${APP_PORT} -w /go/src/app golang:${GO_VERSION} go run main.go

.PHONY: run_image
run_image: image
	$(call blue, "# Running Docker Image Locally...")
	@docker run -it --rm --name ${APP_NAME} -p ${LOCAL_PORT}:3000 ${USERNAME}/${APP_NAME}:${IMAGE_VERSION} 

.PHONY: test
test:
	$(call blue, "# Testing Golang Code...")
	@docker run --rm -it -v "$(GOPATH):/go" -v "$(CURDIR)":/go/src/app -w /go/src/app golang:${GO_VERSION} sh -c 'go test -v -race ${GO_FILES}' 

.PHONY: clean
clean: 
	@rm -f ${app_name} 

#### FUNCTIONS ####
define blue
	@tput setaf 4
	@echo $1
	@tput sgr0
endef
