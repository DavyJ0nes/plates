# Templates

## Description

A selection of template files for new projects, including Dockerfiles, Makefiles, READMEs etc

## Usage

There is a helper tool `get-template` that accompanies this repo to aid in the moving of templates

### Building the tool

```shell
### There is a make file that uses docker to compile the tool and move it to your $HOME/bin directory
make install
```

```shell
# List out templates
get-template -list
Dockerfile.go.example
Dockerfile.python.example
Makefile.go.example
Makefile.python.example
README.example

# Copy Template to Current Directory
get-template -file Dockerfile.go.example
Created Dockerfile
```

## TODO

- [ ] Add Node Makefile and Dockerfile
- [ ] Add Packer.json template
- [ ] Add Jenkinsfile template
- [ ] Add go test file template
- [ ] Add python test file template
- [ ] Add post mortem doc template
- [ ] Add Kubernetes service, deployment, etc templates
- [ ] Add docker-compose template
- [ ] Add bash script template
- [ ] Add go main function template
- [ ] Add Python boto script template
- [ ] Add Prometheus config file template
- [ ] Test Suite for get-template tool

## License

MIT
