# Sample swagger app

# FastAPI Project Setup Guide

## Project Structure
- FastAPI application with Swagger documentation
- Nginx configuration with security headers 
- Docker setup with persistent volumes
- Proper Python package structure
- Logging directory

## Configuration
- Docker Compose with multiple services:
  - FastAPI
  - Nginx 
  - PostgreSQL
  - Adminer
- Nginx configuration with security best practices
- Environment variables setup

## Security Features
- Non-root user in Docker
- Security headers in Nginx
- CORS configuration 
- Environment variable management

## Getting Started

1. Create a `.env` file based on `.env.example` (you'll need to create this manually with appropriate values)

2. Build and start the containers:
