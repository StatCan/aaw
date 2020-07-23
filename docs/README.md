# End-User Documentation

This folder provides the source for the [COVID-19 Advanced Analytics Workspace
Documentation][aaw-docs], which guides users through the major services of the
platform.

## Contributing

Contribution to this documentation, in the official language of your choice, is
welcome. We provide some commands (`make` targets) to make getting started easy,
but please note that **our development tooling is only tested on Ubuntu Linux
with a Bash shell.**

### Prerequisites

The following software needs to be available on your system. Our scripts won't
install these for you because they generally require super-user and we don't
want that much responsibility. :wink:

- GNU Make (e.g. `apt install make`)
- [Node.js][] (e.g. see [`nvm-sh/nvm`][nvm-installation])
- npm (comes with Node.js)
- Python 3.x (e.g. `apt install python3`)
- Python venv module (e.g. `apt install python3-venv`)

### Get Started

1. Ensure you have the above prerequisites
2. Clone this repository
3. Change directory to project root
4. Install remaining dependencies: `make install`
5. <!-- markdownlint-disable no-inline-html -->
   Start a docs server in the language of your choice: `make serve-en` or
   `make serve-fr` (<kbd>CTRL</kbd>+<kbd>C</kbd> to quit)
   <!-- markdownlint-enable -->

You can now see your rendered documentation at `http://localhost:8000` and it
should automatically update when you edit/save your files.

### Submit Your Work

Your documentation needs to pass some checks in order to be accepted. You can
run these checks anytime using `make test`, which will alert you of things like
formatting and spelling issues that need to be addressed.

_Note: These checks are also run as a pre-commit hook, so your commit will be
aborted if they fail._

Once your documentation is ready, just submit a pull request to the `master`
branch of this repository. Your contribution will be published to the
[documentation site][aaw-docs] as soon as it's accepted.

[aaw-docs]: https://statcan.github.io/daaas/
[node.js]: https://nodejs.org/
[nvm-installation]: https://github.com/nvm-sh/nvm#installing-and-updating
