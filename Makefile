BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

progression-pack:
	@echo "$(BOLD)Pulling data from airtable...$(RESET)"
	@python3 ./bin/pull-data.py
	@echo "Progression Data downloaded!"
	@echo "--------------------------------------------------------"
	@echo "$(BOLD)Creating team...$(RESET)"
	@python3 ./bin/create-people.py
	@echo "--------------------------------------------------------"
	@echo "$(BOLD)Creating seniority levels...$(RESET)"
	@python3 ./bin/create-levels.py
	@echo "--------------------------------------------------------"
	@echo "Progression Pack is ready to roll."
	@echo "Run '$(BOLD)bundle exec jekyll serve$(RESET)' to preview"
	@echo "--------------------------------------------------------"

build: progression-pack
	@echo "Build for production"
	# bundle exec jeykll serve
