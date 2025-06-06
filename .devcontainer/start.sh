#!/usr/bin/env bash
set -e

# Move to project root directory
cd "$(dirname "$0")/.."

# Create logs directory if it doesn't exist
mkdir -p logs

# Start logging
echo "[start.sh] Starting up..." | tee -a logs/init.log

# Optional: install frontend dependencies (can be skipped if handled in devcontainer)
echo "[start.sh] Installing frontend dependencies..." | tee -a logs/init.log
(cd frontend && npm install)

# Set Vite API base URL
export VITE_API_BASE="http://localhost:5000"

# Start frontend
echo "[start.sh] Starting frontend..." | tee -a logs/init.log
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

# Give Vite time to bind to port 5173
sleep 8

# Start backend
echo "[start.sh] Starting backend..." | tee -a logs/init.log
(cd backend && nohup python3 app.py >> logs/backend.log 2>&1 &)

# Final log message
echo "[start.sh] Done." | tee -a logs/init.log
