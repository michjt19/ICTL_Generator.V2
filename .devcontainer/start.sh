#!/usr/bin/env bash
set -e

# Create log directory if it doesn't exist
mkdir -p /workspace

echo "🚀 Starting backend (Flask)..."
(cd backend && nohup python3 app.py >> /workspace/backend.log 2>&1 &)

echo "🚀 Starting frontend (React)..."
(cd frontend && nohup npm run dev >> /workspace/frontend.log 2>&1 &)

echo "✅ Both servers started! Logs in /workspace/"
