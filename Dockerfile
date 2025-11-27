FROM python:3.14-slim

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container    
WORKDIR /usr/src

# Copy any source file(s) required for the action
COPY entrypoint.py .

# Make the script executable
RUN chmod +x entrypoint.py

# Configure the container to be run as an executable
ENTRYPOINT ["python3", "/usr/src/entrypoint.py"]