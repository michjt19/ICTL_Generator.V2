#!/usr/bin/env bash
set -e

mkdir -p logs

echo "[start.sh] Starting frontend..." | tee -a logs/init.log
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

# Wait for Vite to bind to port 5173
sleep 8

echo "[start.sh] Starting backend..." | tee -a logs/init.log
(cd backend && nohup python3 app.py >> ../logs/backend.log 2>&1 &)

echo "[start.sh] Done." | tee -a logs/init.log
