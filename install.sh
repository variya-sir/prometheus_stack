#!/bin/bash
echo "Setup local development"

echo "Create .env file"
cp .env.example .env

echo "Export secret variables from .env to .yml files"
set -a ; source .env; envsubst < alertmanager/alertmanager.yml.in > alertmanager/alertmanager.yml