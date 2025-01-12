# Use the official Azure Functions Python image
FROM mcr.microsoft.com/azure-functions/python:4-python3.9

# Update and install additional system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc unixodbc-dev curl gnupg2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Azure Functions Core Tools
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ focal main" > /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && apt-get install -y azure-functions-core-tools-4 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the Azure Function App code to the container
COPY . /home/site/wwwroot

# Set the working directory
WORKDIR /home/site/wwwroot

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Azure Functions host port
EXPOSE 8080

# Command to run the Azure Functions Host
CMD ["func", "host", "start", "--verbose"]

