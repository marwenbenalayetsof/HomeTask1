#!/bin/bash

# Build Docker image
docker build -t test-image:latest .

# Apply Kubernetes deployment
kubectl apply -f app_deployment.yaml