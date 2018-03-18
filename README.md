# File templates

[![Go Report Card](https://goreportcard.com/badge/github.com/DavyJ0nes/templates)](https://goreportcard.com/report/github.com/DavyJ0nes/templates)

## Description

A selection of template files that can easily be copied into projects, including Dockerfiles, Makefiles, READMEs etc

The motivation behind this was to help speed up my workflow and encourage reuse.

If you have any suggestions for improving the templates or want to have some added then please open an [Issue](https://github.com/DavyJ0nes/templates/issues/new) or [Pull Request](https://github.com/DavyJ0nes/templates/compare)

## Usage

### Setup Environment Variables

Before using the tool you will need to get the Environment Variable `TEMPLATE_DIRECTORY` to the location of your templates.

If you are using the default durectory that is within this repo then you can easily set this by running `export TEMPLATE_DIRECTORY=$PWD/templates` on a unix based system.
On Windows you can run `setx TEMPLATE_DIRECTORY "%cd%\templates"`

### Building the tool

```shell
### There is a make file that uses docker to compile the tool and move it to your $HOME/bin directory
$ make install
```

### Running the tool

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
- [x] Python boto script template
- [x] Python boto script test template
- [x] Kubernetes service, deployment, etc templates
- [x] Cloudformation templates
- [x] docker-compose template
- [x] Prometheus config file template
- [x] post mortem doc template
- [ ] Node Makefile and Dockerfile
- [ ] Terraform templates
- [ ] Spinnaker templates
- [ ] Sceptre templates
- [ ] Troposphere templates
- [ ] Golang aws-sdk template

## License

[Apache 2.0](./LICENSE)
