# Copyright (C) 2025 Jasper Boom. All rights reserved.
#
# Proprietary and confidential. Unauthorized use, copying, modification,
# distribution, reverse engineering, disclosure, or creation of derivative
# works is strictly prohibited without prior written permission from
# Jasper Boom.

# -----------------------------
# Variables.
# -----------------------------
SHELL := /bin/bash
BLACK_PYTHON_VERSION ?= py38

# -----------------------------
# Include environment variables file.
# -----------------------------
ifneq (,${wildcard .env})
	include .env
	export
endif

# -----------------------------
# Helper targets
# -----------------------------
.PHONY: help
help: ## Show this help page.
	@echo "Available targets:"
	@grep -hE '^[a-zA-Z0-9_-]+:.*?##' ${MAKEFILE_LIST} | \
		awk -F':.*?##' '{ \
			printf "\033[38;2;67;176;42m  make %-22s\033[0m - \033[38;2;108;172;228m%s\033[0m\n", $$1, $$2 \
		}' | sort

.PHONY: version
version: ## Show the version of this repository.
	@echo "Makefile version: v${VERSION}"

# -----------------------------
# Black formatter targets
# -----------------------------
.PHONY: black
black: ## Run black formatter on repository Python files.
	@echo "Running black formatter on Python files..."
	@apptainer exec \
		--containall \
		--bind ${PWD}:/src \
		docker://${BLACK_IMG}:${BLACK_IMG_TAG} \
		black \
			--line-length 79 \
			--target-version ${BLACK_PYTHON_VERSION} \
			/src