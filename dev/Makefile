IMAGE_NAME := aaw-dev-docs:0.1.0

.DEFAULT_GOAL := create

.PHONY: devlocal

create: build
	./create_diagrams.sh

build: Dockerfile
	docker build . -t $(IMAGE_NAME)

dev/%: build
	$(eval FILEPATH = $(shell find . -name "*$(notdir $@.py)"))
	$(eval DIRNAME = $(shell dirname $(FILEPATH)))
	$(eval BASENAME = $(notdir $@.png))
	inotifywait -m $(FILEPATH) -e modify | while read path action file; do \
		docker run -v $(shell pwd)/:/tmp/ $(IMAGE_NAME) $(FILEPATH); \
		mv $(BASENAME) $(DIRNAME)/$(BASENAME); \
	done;