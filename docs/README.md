# Advanced Analytics Workspace Documentation!

## Introduction

This repository houses the source for the documentation, which provides guidance for using the platform's major services.

We welcome contributions to this documentation in the official language of your choice. We provide commands to make getting started easy. If you're interested in contributing, please follow the instructions below:

## Prerequisites

Ensure that you have the following software available on your system before you begin contributing:

- GNU Make (e.g. `apt install make`)
- Node.js (e.g. see [nvm-installation](https://github.com/nvm-sh/nvm#installing-and-updating))
- npm (comes with Node.js)
- Yarn (e.g. `npm install --global yarn`)
- Python 3.x (e.g. `apt install python3`)
- Python venv module (e.g. `apt install python3-venv`)

Our scripts won't install these for you because they generally require super-user privileges.

## Get Started

Follow these steps to get started contributing:

1. Ensure that you have the prerequisites.
2. Clone this repository.
3. Change the directory to the project root.
4. Install the remaining dependencies with the command `make install`.
5. Start a docs server in the language of your choice by running `make serve-en` or `make serve-fr` (and use <kbd>CTRL</kbd>+<kbd>C</kbd> to quit).

Now you can view your rendered documentation at `http://localhost:8000`. It will automatically update when you edit or save your files.

## Submit Your Work

Your documentation needs to pass some checks to be accepted. You can run these checks anytime using the `make test` command, which will alert you to formatting and spelling issues that need to be addressed. Please note that these checks are also run as a pre-commit hook, so your commit will be aborted if they fail. Once your documentation is ready, submit a pull request to the `master` branch of this repository. Your contribution will be published to the [documentation site][aaw-docs] as soon as it's accepted.

## Translation Workflow

To support maintaining English and French versions of this documentation, we adopt the following workflow for translating content:

1. Merge approved English pull requests to `master` as they become available.
2. Periodically the development team will open an issue to request translation from abhinavgurung. This translation request will be for all English content changes that occurred between the last English commit on the `master` branch that has previously been translated and the present.
3. Translations will always be done in chronologically ordered batches (no cherry-picking of translations).

To keep track of what has previously been translated, we will maintain the long-running feature branch `translated-to-french`, which will point to the most recent commit on `master` that has been translated. When doing a new translation, the translator will look at the diff of `git diff origin/translated-to-french origin/(SOME_COMMIT_ON_MASTER)` (where the commit on `master` is likely the latest commit) to see what English changes have occurred since the last translation. This will help the translator to identify which new English content requires translation to French. During translation, the translator should check out the **most recent** commit on `master` and modify the French content from there. They should not start from the `translated-to-french` branch (as this might be missing some new French content). To commit completed French translation content, the translator should cherry-pick the new French content and merge it into the most recent `master`, but not overwrite the current `master`

[aaw-docs]: https://statcan.github.io/aaw/
[node.js]: https://nodejs.org/
[nvm-installation]: https://github.com/nvm-sh/nvm#installing-and-updating
