#!/bin/bash

TRUE="covid.cloud.statcan.ca"
FAKE="example.ca"

find . -type f -name '*.md' | tee >(xargs sed -i "s/$FAKE/$TRUE/g")
