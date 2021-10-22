#!/usr/bin/env bash

VERSION=$(date +%s)

docker build . -t cat:${VERSION} && \
	docker run --rm -i -t cat:${VERSION}
