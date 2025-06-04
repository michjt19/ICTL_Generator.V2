
import React from "react";
import { Outlet, Link } from "react-router-dom";

export default function SidebarLayout() {
  return (
    <div style={{ display: "flex" }}>
      <nav style={{ width: "200px", padding: "1rem", background: "#eee" }}>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/view">View Tasks</Link></li>
          <li><Link to="/generate">Generate Packet</Link></li>
          <li><Link to="/help">Help</Link></li>
        </ul>
      </nav>
      <main style={{ flexGrow: 1, padding: "1rem" }}>
        <Outlet />
      </main>
    </div>
  );
}
