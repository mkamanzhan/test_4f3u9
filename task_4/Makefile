VENV := .venv/bin/
LOCAL_APP_URL := http://localhost:8000

help:
	clear
	@echo "================= Usage ================="
	@echo "docker-build     to build the docker image"
	@echo "docker-start     to start the docker containers"
	@echo "docker-restart   to restart the docker containers with build image"
	@echo "docker-stop      to stop the docker containers"
	@echo "start            to start the application"
	@echo "test             to run the tests"
	@echo "request-health   to make a request to the health endpoint"

#################
# Docker commands
#################

docker-build:
	docker compose build

docker-start:
	docker compose up -d

docker-restart:
	docker compose down
	docker compose build
	docker compose up -d

docker-stop:
	docker compose down

################
# Local commands
################

start:
	$(VENV)python main.py

format:
	$(VENV)black src tests main.py
	$(VENV)isort src tests main.py
	$(VENV)ruff check --fix src tests main.py
	echo "All formatting done!"

checks:
	$(VENV)bandit -r src
	$(VENV)isort src tests main.py --check
	$(VENV)black src tests main.py --check
	$(VENV)mypy src tests main.py
	$(VENV)ruff check src tests main.py
	echo "All checks passed!"

################
# Request commands
################

request-health:
	curl -s -X GET $(LOCAL_APP_URL)/health | pdm run python -m json.tool


tag := animals
request-content:
	curl -s -X GET $(LOCAL_APP_URL)/taggedContent?tag=$(tag) | pdm run python -m json.tool
