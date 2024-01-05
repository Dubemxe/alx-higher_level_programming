#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the URL from the command-line arguments
url=$1

# Use curl to send a request and get the size of the response body
response_size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

# Check if the Content-Length header is present in the response
if [ -n "$response_size" ]; then
    echo "Size of the response body: ${response_size} bytes"
else
    echo "Unable to determine the size of the response body."
fi
