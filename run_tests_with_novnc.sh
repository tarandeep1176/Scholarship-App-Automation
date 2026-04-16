#!/bin/bash

# Stop any running containers
echo "Stopping any running containers..."
docker compose down --remove-orphans

# Start the Chrome container
echo "Starting chrome container..."
docker compose up -d chrome

# Wait for container to be ready
echo "Waiting for Chrome to be ready..."
sleep 8

# Open browser
echo "Opening noVNC viewer in browser with auto-connect..."

xdg-open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" \
|| open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" \
|| start "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" \
|| echo "Browser open skipped (CI environment)"

# Run tests
echo "Running tests..."
docker compose run --rm selenium-tests

# Create folders
mkdir -p allure-results screenshots assets