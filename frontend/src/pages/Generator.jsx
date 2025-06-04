import React, { useState } from "react";
import axios from "axios";

// ✅ Set your full Codespaces backend URL
const API_BASE = "https://solid-capybara-6p74q67w5wj2g6x-5000.app.github.dev";

export default function Generator() {
  const [code, setCode] = useState("");
  const [status, setStatus] = useState("");

  const handleGenerate = async () => {
    try {
      // Fetch task details from backend
      const res = await axios.get(`${API_BASE}/api/task?code=${code}`);
      const task = res.data;

      // Send task data to backend to generate packet
      const packetRes = await axios.post(`${API_BASE}/api/generate`, { task });

      setStatus("✅ Training packet generated and logged.");
    } catch (err) {
      console.error(err);
      setStatus("❌ Error generating packet.");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Generate Training Packet</h2>
      <input
        type="text"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Enter Task Code (e.g., 081-000-0016)"
        style={{ padding: "0.5rem", marginRight: "1rem", width: "250px" }}
      />
      <button onClick={handleGenerate} style={{ padding: "0.5rem 1rem" }}>
        Generate
      </button>
      <p style={{ marginTop: "1rem" }}>{status}</p>
    </div>
  );
}
