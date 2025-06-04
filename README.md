
# ICTL Training Generator

The ICTL Training Generator is a full-stack web application designed for generating training packets for any Individual Critical Task List (ICTL) task across the 68 Career Management Field (CMF). It enables Soldiers, NCOs, and trainers to search for tasks, extract training standards, and export mission-ready documents for sustainment and evaluation.

---

## 🔧 Features

- ✅ Search STP-based tasks by ICTL code (e.g., `081-000-0016`)
- 📄 Generate Word, Excel, PDF, and PowerPoint packets
- 🧠 Built-in parser for per-task extraction from official STPs
- 📁 Log export history with timestamps and file details
- 🌓 Dark mode toggle and rotating quotes on homepage
- 🚀 React frontend with Flask backend (GitHub Codespaces compatible)

---

## 📦 Project Structure

```
📁 backend/
  ├── app.py                 # Flask API
  ├── parser/                # Task parser
  ├── generate_docs/         # Packet generators
  ├── static/STPs/           # Upload STPs here
  └── logs/packet_log.json   # Version tracking

📁 frontend/
  ├── public/                # HTML template
  ├── src/pages/             # Home, TaskViewer, Generator, Help
  ├── src/components/        # Sidebar layout
  └── vite.config.js         # React-to-Flask proxy

📁 data/tasks/               # Parsed .json storage (future use)
```

---

## 🚀 How to Launch in GitHub Codespaces

1. Create a new GitHub repo and upload all files.
2. Click **“Code” > “Open with Codespaces”**.
3. In Codespaces Terminal:

```bash
# Backend
pip install -r backend/requirements.txt
python backend/app.py
```

```bash
# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

4. Make ports 3000 (frontend) and 5000 (backend) public.

---

## 🌐 Deploy to GitHub Pages

To deploy the frontend only:
1. Add to `frontend/package.json`:

```json
"homepage": "https://YOUR_USERNAME.github.io/ICTL-Training-Generator"
```

2. Add deploy scripts:

```json
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d dist"
}
```

3. Deploy:

```bash
npm install gh-pages --save-dev
npm run deploy
```

---

## 📎 Notes

- Backend STP parsing is offline/local — place official STPs inside `backend/static/STPs/`
- Task generation is logged in `logs/packet_log.json`
- This project is public and open to contributions.

---

## 📄 License

MIT License. Created for mission optimization, training readiness, and automation support within the U.S. Army Medical field.

---

## 🤝 Maintainer

Developed with the assistance of AI to support Soldier readiness and streamline training operations.

