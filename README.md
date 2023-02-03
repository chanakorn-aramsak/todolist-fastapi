# todolist-fastapi

# todolist-fastapi with .devcontainer

An example `Dockerfile` for a FastAPI app with a few dependencies:

 * Python 3.x
 * FastAPI
 * uvicorn
 * [manage-fastapi](https://github.com/ycd/manage-fastapi)

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

## Running fastapi app

1. Open a terminal window in Visual Studio Code

2. Navigate to the project directory where `main.py` is located

3. Run the following command:

    ```fastapi run```

This command will run the uvicorn server and start the application with hot reloading enabled. This means that if you make any changes to your code, the server will automatically reload and reflect those changes.


# Installing Package with pip and Updating requirements.txt

To install a package using pip and update the requirements.txt file in one line, you can use the following command:

```pip install <package_name> && pip freeze > requirements.txt```


