import React, { useState } from "react";
import axios from "axios";

// Use environment variable so the frontend works in any environment
const API_BASE = import.meta.env.VITE_API_BASE || "";

export default function Generator() {
  const [code, setCode] = useState("");
  const [status, setStatus] = useState("");
  const [task, setTask] = useState(null);

  const handleGenerate = async () => {
    setStatus("Loading...");
    setTask(null);

    try {
      const res = await axios.get(`${API_BASE}/api/task?code=${code}`);
      setTask(res.data);

      await axios.post(`${API_BASE}/api/generate`, { task: res.data });

      setStatus("✅ Training packet generated and logged.");
    } catch (err) {
      console.error(err);
      setStatus("❌ Error generating packet or task not found.");
    }
  };

  return (
    <div className="generator">
      <h2>🎯 Generate Training Packet</h2>

      <input
        className="task-input"
        type="text"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Enter Task Code (e.g. 081-000-0016)"
      />

      <button className="primary-btn" onClick={handleGenerate}>
        Generate
      </button>

      <p>{status}</p>

      {task && (
        <div className="task-card" style={{ marginTop: "2rem" }}>
          <h3>{task.title}</h3>
          <p><strong>Condition:</strong> {task.condition}</p>
          <p><strong>Standard:</strong> {task.standard}</p>
        </div>
      )}
    </div>
  );
}
