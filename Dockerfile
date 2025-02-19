# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install OS dependencies and clean up cache
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && apt-get clean

# Copy the requirements file and install dependencies
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY ./app .

# Expose port 7000 and run the application
EXPOSE 7000
CMD ["python", "app.py"]
