
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);

// Dark mode toggle
const toggle = document.createElement('button');
toggle.innerText = "🌓 Toggle Dark Mode";
toggle.onclick = () => document.body.classList.toggle('dark');
toggle.style.position = 'fixed';
toggle.style.bottom = '1rem';
toggle.style.right = '1rem';
toggle.style.zIndex = 1000;
document.body.appendChild(toggle);
