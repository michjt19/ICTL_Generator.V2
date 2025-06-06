#!/usr/bin/env bash
set -e

# Start backend
(cd backend && nohup python app.py >/workspace/backend.log 2>&1 &)

# Start frontend
(cd frontend && nohup npm run dev >/workspace/frontend.log 2>&1 &)

