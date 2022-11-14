help: ## Show help for each command
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

install: ## Install local development
	./install.sh

run: ## Run prometheus stack
	docker-compose up

clean: ## Clean up prometheus stack
	docker-compose down -v
