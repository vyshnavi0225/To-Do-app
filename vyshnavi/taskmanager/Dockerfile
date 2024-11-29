# Use a lightweight Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install  -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8080

# Set the entrypoint for the container to run the Flask app
CMD ["python", "app.py"]
