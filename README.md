# Books library API demo  

This repository contains example code for a RESTful API based on Flask and Flask-RESTx in Python.

Code implements RESTful API for books library management

The code of this demo app is composed from code of two projects:
1. http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
2. https://github.com/kajpawl/flaskLibraryApi

It makes use of:
* Python 3
* Flask
* Swagger UI (via `restx`)
* Simple SQL model (`SQLAlchemy`)
* Alpine Linux (if running as a docker container)

#### Running project
1. Docker must be installed and run
2. Change to the root of working directory, where Makefile is placed
3. `make build`
4. `make run`
5. Browse API in the browser at `http://localhost:8000/api/`





