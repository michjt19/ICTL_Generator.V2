import React from "react";
import { Outlet, Link } from "react-router-dom";

export default function SidebarLayout() {
  const toggleDark = () => document.body.classList.toggle("dark");

  return (
    <div className="app-container">
      <nav className="sidebar">
        <h2>ICTL Generator</h2>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/view">View Tasks</Link></li>
          <li><Link to="/generate">Generate Packet</Link></li>
          <li><Link to="/help">Help</Link></li>
        </ul>
        <button className="dark-toggle" onClick={toggleDark}>🌓 Theme</button>
      </nav>
      <main className="main">
        <Outlet />
      </main>
    </div>
  );
}
