#!/bin/bash

# Define the API URL
API_URL="http://127.0.0.1:5000/predict"

# Create JSON input with test data
JSON_DATA='{"features": [5.1, 3.5, 1.4, 0.2]}'

# Send a POST request to the API
curl -X POST "$API_URL" -H "Content-Type: application/json" -d "$JSON_DATA"
