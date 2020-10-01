# TVDB Serverless Functions

OpenFaaS Serverless functions for TVDB. The functions use the [python3-fastapi](https://github.com/loudsquelch/openfaas-python3-fastapi-template) template, which provides the following advantages:

* Request and Response schema are defined as Pydantic models. 
* These models contain nested schema generated from the TVDB API v3 Swagger spec.
* All data operations are type-checked at runtime, and type/schema errors will be provided in the HTTP response. 
* Interactive API documentation is provided using the Swagger UI at the `GET` route for each function. 

## Installation

A more thorough guide will come later. For now, just have a kubernetes cluster with OpenFaaS ready to go, and make sure you have access to the OpenFaaS gateway. 

### Pull template

To pull the `python3-fastapi` template:

```
faas-cli template pull stack
```

### Build functions

To build a function, use the corresponding `faas-cli` command. For example:

```
faas-cli build -f tvdb-auth-token.yml
```

### Deploy functions

To deploy a function, use the corresponding `faas-cli` command. For example:

```
faas-cli up -f tvdb-auth-token.yml
```