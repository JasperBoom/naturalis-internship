# Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.

# -----------------------------
# Variables
# -----------------------------
SHELL := /bin/bash

# Include the .env file.
ifneq (,${wildcard .env})
	include .env
	export
endif

# Include common makefile definitions and functions.
include Makefile.common