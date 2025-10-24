
# Deployment Guide — Quick Demo Deployment Options

## Lightweight options (for hackathon demo)
- **Streamlit Cloud or Vercel** for frontend (static build) and **Render / Railway** for backend.
- If using Vercel, build frontend and point API calls to the hosted backend URL.

## Steps for Render (example)
1. Push repo to GitHub.
2. Create Render service for backend (Python): Set build command `pip install -r app/requirements.txt` and start `uvicorn app.main:app --host 0.0.0.0 --port 8000`
3. Create Vercel project for frontend and set API base URL env var to Render backend URL.

## Using Docker on a VPS
- Build images locally and push to Docker Hub or registry.
- On VPS: `docker-compose up -d` and configure firewall accordingly.
- Use a reverse proxy (Nginx) if hosting multiple services on port 80/443.

## Environment variables
- `GANACHE_URL` - RPC endpoint for Ganache
- `DATABASE_URL` - sqlite file path or connection string
- `SECRET_KEY` - JWT secret (if adding auth)
