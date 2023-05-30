# AAW Developer Documentation

Developer-facing documentation that covers the major features of the AAW platform.


# How to Contribute

## Update the Diagrams

Diagrams are created using the [Diagrams](https://diagrams.mingrammer.com/) Python package. To update the diagrams for this repo, simply run `make` at the root of the repository to find all `*.py` files and build the corresponding `*.png` file for each one.

## Develop a diagram

Create a new diagram with a unique name in the `/docs` folder.

Run the below `make target`
```
make dev/diagram_name
```
replacing `diagram_name` with the name of your new diagram (excluding the `.py` file extension).
This `make dev/diagram_name` will rebuild the diagram each time you save the corresponding python file.
