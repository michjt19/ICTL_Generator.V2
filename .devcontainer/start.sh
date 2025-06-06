#!/usr/bin/env bash
set -e

mkdir -p logs

echo "[start.sh] Installing frontend dependencies..." | tee -a logs/init.log
(cd frontend && npm install)

echo "[start.sh] Starting frontend..." | tee -a logs/init.log
export VITE_API_BASE="http://localhost:5000"
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

sleep 8

echo "[start.sh] Starting backend..." | tee -a logs/init.log
(cd backend && nohup python3 app.py >> ../logs/backend.log 2>&1 &)

echo "[start.sh] Done." | tee -a logs/init.log
