
import React, { useState } from "react";
import axios from "axios";

export default function Generator() {
  const [code, setCode] = useState("");
  const [status, setStatus] = useState("");

  const handleGenerate = async () => {
    try {
      const res = await axios.get(`/api/task?code=${code}`);
      const task = res.data;
      const packetRes = await axios.post("/api/generate", { task });
      setStatus("Training packet generated and logged.");
    } catch (err) {
      setStatus("Error generating packet.");
    }
  };

  return (
    <div>
      <h2>Generate Training Packet</h2>
      <input type="text" value={code} onChange={(e) => setCode(e.target.value)} placeholder="Task code" />
      <button onClick={handleGenerate}>Generate</button>
      <p>{status}</p>
    </div>
  );
}
