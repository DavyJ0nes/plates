# File templates
[![Go Report Card](https://goreportcard.com/badge/github.com/DavyJ0nes/templates)](https://goreportcard.com/report/github.com/DavyJ0nes/templates)

## Description

A selection of template files for new projects, including Dockerfiles, Makefiles, READMEs etc

## Usage

There is a helper tool `file-templates` that accompanies this repo to aid in the moving of templates

### Building the tool

```shell
### There is a make file that uses docker to compile the tool and move it to your $HOME/bin directory
$ make install
```

```shell
# List out templates
$ file-templates list
1.      Dockerfile-python
2.      post-mortem.md
3.      Dockerfile-go
4.      bash_script.sh
5.      docker-compose.yml

# Copy Template to Current Directory
$ file-templates copy Dockerfile-go Dockerfile

# get version information
$ file-templates version
Version:        0.1.0
Git Hash:       515f3d
Build Time:     2018-03-18_11:42:58AM
```

## TODO

- [x] Packer.json template
- [x] Jenkinsfile template
- [x] go main function template
- [x] go test file template
- [x] bash script template
- [x] python script template
- [x] python script test template
- [ ] Python boto script template
- [ ] Python boto script test template
- [x] Kubernetes service, deployment, etc templates
- [x] Cloudformation templates
- [x] docker-compose template
- [x] Prometheus config file template
- [ ] Node Makefile and Dockerfile
- [x] post mortem doc template

## License

MIT