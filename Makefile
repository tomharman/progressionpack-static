#!/usr/bin/env bash

BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

pp:
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
	@echo "$(BOLD)Creating goals...$(RESET)"
	@python3 ./bin/create-goals.py
	@echo "--------------------------------------------------------"
	@echo "Progression Pack is ready to roll."
	@echo "--------------------------------------------------------"

# For open information

build: pp
	@echo "$(BOLD)Building for production$(RESET)"
	JEKYLL_ENV=production bundle exec jekyll build

serve: pp
	@echo "$(BOLD)Watching...$(RESET)"
	JEKYLL_ENV=production bundle exec jekyll serve

# For team-safe environments

build-teamsafe: pp
	@echo "$(BOLD)Building for Team Safe Environment$(RESET)"
	JEKYLL_ENV=teamsafe bundle exec jekyll build

serve-teamsafe: pp
	@echo "$(BOLD)Watching...$(RESET)"
	JEKYLL_ENV=teamsafe bundle exec jekyll serve