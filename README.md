# File templates

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
```

## TODO

- [x] Add Packer.json template
- [x] Add Jenkinsfile template
- [x] Add go main function template
- [x] Add go test file template
- [x] Add bash script template
- [x] Add python script template
- [x] Add python script test template
- [ ] Add Python boto script template
- [ ] Add Python boto script test template
- [ ] Add Kubernetes service, deployment, etc templates
- [x] Add docker-compose template
- [x] Add Prometheus config file template
- [ ] Add Node Makefile and Dockerfile
- [x] Add post mortem doc template
- [ ] Test Suite for get-template tool

## License

MIT