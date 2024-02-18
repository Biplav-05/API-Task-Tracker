FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /backend-api

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container at /app/
COPY ./requirements.txt /backend-api/requirements.txt

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt

# Copy the content of the local app directory to the working directory
COPY . /backend-api/
RUN chmod +x /backend-api/entrypoint.sh

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run on container start
CMD ["/bin/sh", "/backend-api/entrypoint.sh"]
