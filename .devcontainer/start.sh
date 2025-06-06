#!/usr/bin/env bash
set -e

# Start backend
(cd backend && nohup python3 app.py >/workspace/backend.log 2>&1 &)

# Expose backend URL for Vite dev server
export VITE_API_BASE="http://localhost:5000"

# Start frontend
(cd frontend && nohup npm run dev >/workspace/frontend.log 2>&1 &)

