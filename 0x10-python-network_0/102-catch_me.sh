#!/bin/bash
# This script makes a request to the server and extracts a message

# Make a request to the server
response=$(curl -s 0.0.0.0:5000/catch_me)

# Check if curl request was successful
if [ $? -ne 0 ]; then
    echo "Error: Curl request failed"
    exit 1
fi

# Extract the message from the response
if [[ $response =~ "You got me!" ]]; then
    message="You got me!"
else
    message="Message not found in response"
fi

# Display the message
printf "%s\n" "$message"

# Test the output as per the provided example
if [ "$message" == "You got me!" ]; then
    exit 0
else
    exit 1
fi
