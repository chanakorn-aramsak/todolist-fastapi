# Use devcontainer for development
# Please note that this image is large (1.46GB), 
# consider using a smaller base image if possible 
# to minimize the size of the final Docker image.

FROM mcr.microsoft.com/devcontainers/python:0-3.11


WORKDIR /code

# Copy the requirements file
COPY requirements.txt /code/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./app /code/app

# Run the application server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
