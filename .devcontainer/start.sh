#!/usr/bin/env bash
set -e

# Create logs directory if it doesn't exist
mkdir -p logs

# Start frontend
echo "[start.sh] Starting frontend..." | tee -a logs/init.log
export VITE_API_BASE="http://localhost:5000"
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

# Wait for Vite to bind to port 5173
sleep 8

# Start backend
echo "[start.sh] Starting backend..." | tee -a logs/init.log
(cd backend && nohup python3 app.py >> ../logs/backend.log 2>&1 &)

echo "[start.sh] Done." | tee -a logs/init.log
