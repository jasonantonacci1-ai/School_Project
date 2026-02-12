#!/bin/bash
# Script to build and push images to Docker Hub for Kubeadm deployment

USERNAME="jasonantonacci1"

set -e

echo "=== Building and Pushing Frontend ==="
docker build -t $USERNAME/frontend:latest ./frontend
docker push $USERNAME/frontend:latest

echo "=== Building and Pushing Student Service ==="
docker build -t $USERNAME/studentservice:latest ./studentservice
docker push $USERNAME/studentservice:latest

echo "=== Building and Pushing Teacher Service ==="
docker build -t $USERNAME/teacherservice:latest ./teacherservice
docker push $USERNAME/teacherservice:latest

echo "=== Building and Pushing Employee Service ==="
docker build -t $USERNAME/employeeservice:latest ./employeeservice
docker push $USERNAME/employeeservice:latest

echo "=== Done! All images pushed to $USERNAME ==="
