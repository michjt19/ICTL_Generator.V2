
import React from "react";

export default function Home() {
  const quotes = [
    "Train hard, fight easy.",
    "Victory favors the prepared.",
    "Readiness is the key to survival.",
    "Every Soldier a medic."
  ];
  const quote = quotes[Math.floor(Math.random() * quotes.length)];

  return (
    <div className="home">
      <h1>Welcome to the ICTL Training Generator</h1>
      <p>{quote}</p>
      <p>Use the navigation to view tasks, generate packets, or get help.</p>
    </div>
  );
}
