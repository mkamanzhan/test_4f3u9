# task_4

## Development Requirements
* Python 3.11.*
* Docker Compose
* PDM(Python Package Manager)

## How to run
Project can be run using Docker Compose or locally.

### Using Docker Compose
```bash
make docker-build
make docker-start
```

### Local Development
Before running the project, you need to install the dependencies using PDM.

Install PDM by this documentation: https://pdm-project.org/en/latest/#installation

Then run the following commands:
```bash
pdm install --dev  # Install the dependencies for development
```

Then you can run the project using the following command:
```bash
pdm run main.py
```

## API Documentation
API documentation can be found at http://localhost:8000/redoc


## How to test endpoints

### Get Health Check
```bash
make request-content
```

### Get Tagged Content
tag: {tag} is the tag you want to search for.
```bash
make request-content tag={tag}
```
