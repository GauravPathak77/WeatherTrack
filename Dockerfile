# Step 1: Set up the base Docker image
FROM python:3.9-slim

# Step 2: Install required dependencies
RUN pip install Flask

# Step 3: Copy the Flask application files into the container
WORKDIR /app
COPY server.py /app

# Step 4: Specify the command to run the Flask application
CMD ["python", "server.py"]
