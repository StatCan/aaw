#!/bin/bash

TRUE="not-telling-you-the-hostname.ca"
FAKE="example.ca"

find . -type f -name '*.md' | tee >(xargs sed -i "s/$TRUE/$FAKE/g")
