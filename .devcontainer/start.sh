#!/usr/bin/env bash
set -e

mkdir -p logs

echo "[start.sh] Starting backend..." | tee -a logs/init.log
(cd backend && nohup python3 app.py >> ../logs/backend.log 2>&1 &)

echo "[start.sh] Waiting before starting frontend..." | tee -a logs/init.log
sleep 5

echo "[start.sh] Starting frontend..." | tee -a logs/init.log
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

echo "[start.sh] Done." | tee -a logs/init.log
