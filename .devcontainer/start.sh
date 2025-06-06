#!/usr/bin/env bash
set -e

# Create log directory inside your repo
mkdir -p logs

echo "🚀 Starting backend (Flask)..."
(cd backend && nohup python3 app.py >> ../logs/backend.log 2>&1 &)

echo "🚀 Starting frontend (React)..."
(cd frontend && nohup npm run dev >> ../logs/frontend.log 2>&1 &)

echo "✅ Both servers started! Logs saved in ./logs/"
