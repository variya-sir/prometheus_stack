#!make
include .env

all: exportenv
		docker compose up

# Export secret variables from .env to .yml files
exportenv:
		set -a ; source .env ; envsubst < alertmanager/alertmanager.yml.in > alertmanager/alertmanager.yml

clean:
		docker-compose down -v
