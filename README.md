# Running the devcontainer
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
