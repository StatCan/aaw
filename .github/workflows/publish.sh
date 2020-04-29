name: Publish

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest
#     strategy:
#       matrix:
#         python-version: [3.5, 3.6, 3.7, 3.8]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 mkdocs mkdocs-material
#        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
#     - name: Lint with flake8
#       run: |
#         # stop the build if there are Python syntax errors or undefined names
#         flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
#         # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
#         flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Build and publish
      run: |
        mkdocs gh-deploy

