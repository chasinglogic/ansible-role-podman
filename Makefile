.PHONY: test

test:
	circleci local execute -e CIRCLE_PROJECT_REPONAME=$(shell basename $(shell pwd)) --job test
