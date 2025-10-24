
# Docker & Docker-Compose Guide

## Overview
Use Docker to containerize backend and frontend for easy demo setup. Ganache can run locally on host or in its own container.

## Files
- `backend/Dockerfile` — builds Python backend
- `frontend/Dockerfile` — builds Node frontend
- `docker-compose.yml` — orchestrates services

## Commands
- Build & run: `docker-compose up --build`
- View logs: `docker-compose logs -f backend`
- Stop: `docker-compose down`

## Notes
- For Ganache, either run locally (recommended during dev) or add a Ganache service in docker-compose (expose port 8545).
- Mount volumes for live code reload during hackathon.
