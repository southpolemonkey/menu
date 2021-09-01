IMAGE := zendesk-bot

build:
	@echo "Building image"
	@docker build -t ${IMAGE} .

run:
	@echo "Run backend..."
	@docker-compose run app

# Dev-related
lint:
	@echo "Linting the repo..."
	@black backend/

test:
	@echo "Testing the repo..."
	@pytest -W ignore -vv backend

pylint:
	@echo "Running pylint..."
	@pylint backend/ --disable=C --disable=W1203 --disable=W1202 --reports=y

radon:
	@echo "Run Radon to compute complexity..."
	@radon cc backend/ --total-average -nb

update-package:
	@echo "Update package"
	@pip freeze > requirements.txt