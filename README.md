![Unit tests](https://github.com/maniknarang/hypothesis-grammar-extension/actions/workflows/python-app.yml/badge.svg)
## Hypothesis Grammar Extension

This project aims to extend property-based testing in Hypothesis by integrating grammar-based input generation. The goal is to create random inputs for functions using grammars (such as regular expressions or Context-Free Grammars), which will help refine input generation to match the expected structure. The extension will provide customizable grammar definitions for common input types (e.g., emails, phone numbers), allowing users to specify their own grammars for input generation. This tool takes in grammars of .cfg or ANTLR .g4 format (examples under `tests/` and `converter/tests/`).

Capstone project/CS230 course project advised by Professor Miryung Kim and Ben Limpanukorn. Project worked on by Andrew Hu, Garrick Su, William Santosa and Manik Narang.

## Running the devcontainer
Install the VS Code [Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. It is recommended that you install [Docker](https://docs.docker.com/desktop/), but it only requires the [Docker Engine](https://docs.docker.com/engine/install/) to be running to launch the devcontainer.

On VS Code, press `ctrl/cmd` + `shift` + `P` to bring up the command palette and run:
```
>Dev Containers: Clone Repository in Container Volume
```

Select this repository and select the `main` branch.

This should open up the devcontainer with everything setup for you. Make sure your VS Code has selected a Python interpretter with
```
>Python: Select Interpreter
```
so that the formatter works.

## Running Tests

1. Follow the steps above to run the devcontainer.
2. Run `pytest` or push code to your branch for code to be tested.

The tests are located under the `tests` directory and are of the format `test_*.py`.

## Key Contributions

- Provide grammar-based input generation for property-based testing in Hypothesis.
- Enable users to define common input formats (e.g., emails, phone numbers) via grammars.
- Allow users to write their own grammars for customized input generation.
- Enhance input generation strategies to improve coverage and bug detection.

## Evaluation Metrics:

1. Test Coverage: Line/branch/path coverage.
2. Bug Detection: Number of bugs discovered.
3. Input Range and Validity: Comparing grammar-based vs. standard Hypothesis inputs.

## Potential Test Domains

1. SQL Tables
2. JSON
3. Math Equations / Expressions (sympy, eval)
4. Graphs
5. Neural Network – testing “transformers” package
6. Compilers
7. Regular Expressions
8. HTTP Headers
9. Cloud Formation
