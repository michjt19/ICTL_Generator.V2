import React, { useEffect, useState } from "react";
import axios from "axios";

// Use environment variable so the frontend works in any environment
const API_BASE = import.meta.env.VITE_API_BASE || "";

export default function TaskViewer() {
  const [tasks, setTasks] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchAllTasks = async () => {
      try {
        const res = await axios.get(`${API_BASE}/api/tasks`);
        setTasks(res.data);
      } catch (err) {
        console.error("Failed to load tasks:", err);
      }
    };

    fetchAllTasks();
  }, []);

  const filtered = tasks.filter(
    (task) =>
      task.code.toLowerCase().includes(search.toLowerCase()) ||
      task.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="task-viewer">
      <h2>📚 Task Viewer</h2>

      <input
        className="search-input"
        type="text"
        placeholder="Search by task code or title"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {filtered.length === 0 ? (
        <p>No tasks found.</p>
      ) : (
        <ul className="task-list">
          {filtered.map((task) => (
            <li key={task.code} className="task-card">
              <h3>{task.code} — {task.title}</h3>
              <p><strong>Condition:</strong> {task.condition}</p>
              <p><strong>Standard:</strong> {task.standard}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
