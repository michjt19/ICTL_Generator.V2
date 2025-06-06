import React from "react";

export default function Help() {
  return (
    <div className="help">
      <h2>Help & Instructions</h2>
      <ul>
        <li>Use "View" to look up ICTL task content from STP PDFs.</li>
        <li>Use "Generate" to export a packet in Word, Excel, PDF, or PPT.</li>
        <li>Ensure STP files are located in the backend/static/STPs/ folder.</li>
      </ul>
    </div>
  );
}
