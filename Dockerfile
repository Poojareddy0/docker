# Start your image with a node base image
FROM python:3.9-alpine

# The /app directory should act as the main application directory
WORKDIR /home/data

# Copying the files into the container
COPY IF.txt AlwaysRememberUsThisWay.txt scripts.py ./

# Install required Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir --upgrade pip \
    && apk del gcc musl-dev libffi-dev

# Create the output folder if it does not exist
RUN mkdir -p output

# Run the Python script
CMD ["python", "/home/data/scripts.py"]