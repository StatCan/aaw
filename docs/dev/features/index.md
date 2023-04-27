# AAW Feature Documentation

This purpose of this section of the documentation is to cover features that are not appropriate to document in a single repository. For example, certain platform features involve many repositories, so their documentation should be centralized in this documentation section to improve discoverability.

Feature documentation should include the following information:

1. A link to the Epic created for the feature (the Epic should have links to all of the sub-issues that were involved in the Epic).
2. Links to all repositories that were involved with the feature along with a short description of the scope of each repository's involvement.
3. Architecture diagrams where appropriate to show how all of the components fit together. Diagrams should be specified as code using the [Python diagrams package](https://diagrams.mingrammer.com/). There is a `Makefile` and a `Dockerfile` under `docs/dev/diagrams`; to create all diagrams, add your diagram name to the `Makefile` and run `make run` in the `docs/dev/diagrams` folder.
4. A short explanation of how the feature works and what the purpose/scope of the feature is.