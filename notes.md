<<<<<<< HEAD
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

- Environment Variables (.env) Best Practices:
  - Never commit .env files to version control
  - Create a .env.example template with dummy values
  - Required variables:
    - DATABASE_URL=postgresql://user:password@host:5432/dbname
    - SECRET_KEY=your-secure-secret-key
    - ENVIRONMENT=development/production
    - ALLOWED_HOSTS=localhost,example.com
  - Use strong, unique passwords
  - Restrict file permissions (chmod 600)
  - Validate all env variables on startup
  - Use type hints and validation with pydantic
  - Keep sensitive data encrypted at rest

- Nginx configuration with security best practices:
  - SSL/TLS configuration
  - Security headers
  - Rate limiting

## Security Features
- Non-root user in Docker
- Security headers in Nginx
- CORS configuration 
- Environment variable management

## Getting Started

1. Create a `.env` file based on `.env.example` (you'll need to create this manually with appropriate values)

2. Build and start the containers:
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
