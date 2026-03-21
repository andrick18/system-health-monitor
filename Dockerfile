# Base image
FROM ubuntu:24.04

# Author
LABEL maintainer="Andrick Diatilo"

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    bash \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY health_check.sh .
COPY alert.py .

# Make the bash script executable
RUN chmod +x health_check.sh

# Default command — run the health check and alert
CMD ["bash", "-c", "./health_check.sh && python3 alert.py"]
