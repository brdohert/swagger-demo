# FastAPI with Nginx and Docker

A modern web application built with FastAPI, Nginx, and Docker, following best practices for security and development.

## Features

- FastAPI backend with automatic Swagger documentation
- Nginx reverse proxy with SSL support
- Docker containerization with persistent volumes
- Secure configuration and best practices
- Development and production environments

## Project Structure

```
.
├── app/                    # FastAPI application
│   ├── api/               # API routes
│   ├── core/              # Core functionality
│   ├── models/            # Data models
│   └── services/          # Business logic
├── nginx/                 # Nginx configuration
├── docker/                # Docker-related files
├── tests/                 # Test files
└── docker-compose.yml     # Docker Compose configuration
```

## Prerequisites

- Docker and Docker Compose
- Python 3.8+ (for local development)
- Git

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - API: http://localhost:8000
   - Swagger UI: http://localhost:8000/docs
   - Adminer: http://localhost:8080

## Development

For local development:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Security Considerations

- All sensitive data is stored in environment variables
- HTTPS is enforced in production
- Regular security updates are applied
- Input validation and sanitization
- Rate limiting implemented
- CORS properly configured

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details 