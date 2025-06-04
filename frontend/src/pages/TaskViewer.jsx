
import React, { useState } from "react";
import axios from "axios";

export default function TaskViewer() {
  const [code, setCode] = useState("");
  const [task, setTask] = useState(null);
  const [error, setError] = useState("");

  const fetchTask = async () => {
    try {
      const res = await axios.get(`/api/task?code=${code}`);
      setTask(res.data);
      setError("");
    } catch (err) {
      setError("Task not found.");
      setTask(null);
    }
  };

  return (
    <div>
      <h2>Search for a Task</h2>
      <input type="text" value={code} onChange={(e) => setCode(e.target.value)} placeholder="e.g., 081-000-0016" />
      <button onClick={fetchTask}>Search</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {task && (
        <div>
          <h3>{task.task_id}</h3>
          <pre>{task.content}</pre>
        </div>
      )}
    </div>
  );
}
