# todolist-fastapi

# todolist-fastapi with .devcontainer

An example `Dockerfile` for a FastAPI app with a few dependencies:

 * Python 3.x
 * FastAPI
 * uvicorn

## Prerequisites

I assume you have installed Docker and Visual Studio Code with the Remote - Containers extension.

See the [Docker website](https://www.docker.com/products/docker-desktop) for installation instructions for Docker.

See the [Visual Studio Code - Remote Development documentation](https://code.visualstudio.com/docs/remote/containers) for installation instructions for the Remote - Containers extension.

## Running the application in a container

1. Clone the repository

        git clone https://github.com/chanakorn-github/todolist-fastapi.git

2. Open the cloned repository in Visual Studio Code

3. Click the "Remote-Containers: Open Folder in Container" command in the Command Palette (press `F1` or `Ctrl`/`Cmd` + `Shift` + `P` to open the Command Palette)

4. Wait for the container to start and for the application to be installed

5. Once everything has started up, you should be able to access the application by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Troubleshooting

If you encounter issues with running the application, try the following steps:

1. Check the status of the container in the Visual Studio Code Terminal. There may be error messages indicating what went wrong.

2. Try rebuilding the container by running the "Remote-Containers: Rebuild Container" command in the Command Palette.

3. If the problem persists, consult the [Visual Studio Code - Remote Development troubleshooting documentation](https://code.visualstudio.com/docs/remote/troubleshooting).
