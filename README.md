# ICTL Training Generator

The ICTL Training Generator is a full-stack web application designed to generate training packets for any Individual Critical Task List (ICTL) task across the 68 Career Management Field (CMF). It enables Soldiers, NCOs, and trainers to search for tasks, extract training standards, and export mission-ready documents for sustainment and evaluation.

---

## 🔧 Features

- ✅ Search STP-based tasks by ICTL code (e.g., `081-000-0016`)
- 📄 Generate Word, Excel, PDF, and PowerPoint packets
- 🧠 Built-in parser for per-task extraction from official STPs
- 📁 Log export history with timestamps and file details
- 🌓 Dark mode toggle and rotating quotes on the homepage
- 🚀 React frontend with Flask backend (fully GitHub Codespaces compatible)

---

## 📦 Project Structure

📁 backend/
├── app.py # Flask API
├── parser/ # Task parser
├── generate_docs/ # Packet generators
├── static/STPs/ # Upload official STPs here
└── logs/packet_log.json # Version tracking

📁 frontend/
├── public/ # HTML template
├── src/pages/ # Home, TaskViewer, Generator, Help
├── src/components/ # Sidebar layout
└── vite.config.js # React-to-Flask proxy

📁 data/tasks/ # Parsed .json storage (future use)

---

## 🚀 Launch in GitHub Codespaces

1. Create a new GitHub repository and upload all files.
2. Click **“Code” → “Open with Codespaces”**.
3. In the Codespaces terminal, run:

### Backend
pip install -r backend/requirements.txt

python backend/app.py

### Frontend (in a new terminal)
cd frontend

npm install

npm run dev


**Open the "Ports" tab and make port 5173 (frontend) and port 5000 (backend) public.**

**If you're using GitHub Codespaces, the included .devcontainer configuration will automatically:**
 - Install dependencies
 - Start both servers
 - Forward the necessary ports
 - Open them in the browser

**The start.sh script sets VITE_API_BASE=http://localhost:5000 before starting the frontend so requests hit your local backend. If the script isn't executable, run:**

chmod +x .devcontainer/start.sh


## 🌐 Deploy to GitHub Pages (Frontend Only)

- **In frontend/package.json, add:**

"homepage": "https://YOUR_USERNAME.github.io/ICTL-Training-Generator"


- **Add deploy scripts:**
  
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d dist"
}


- **Deploy with:**

npm install gh-pages --save-dev

npm run deploy


## 📎 Notes
- STP parsing is done locally — upload official STPs to backend/static/STPs/.

- Training packet generation activity is logged in logs/packet_log.json.

- This project is public and open to contributions.

## 📄 License
- MIT License. Created to support mission optimization, training readiness, and automation within the U.S. Army Medical field.

## 🤝 Maintainer
- Developed with the assistance of AI to support Soldier readiness and streamline training operations.

---

Let me know if you'd like:
- A `CONTRIBUTING.md` file for collaborators
- A badge section (`build`, `version`, `license`, etc.)
- Screenshots or a walkthrough GIF for the homepage!






