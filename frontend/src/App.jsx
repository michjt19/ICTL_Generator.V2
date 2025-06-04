
import { Routes, Route } from "react-router-dom";
import SidebarLayout from "./components/SidebarLayout";
import Home from "./pages/Home";
import TaskViewer from "./pages/TaskViewer";
import Generator from "./pages/Generator";
import Help from "./pages/Help";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<SidebarLayout />}>
        <Route index element={<Home />} />
        <Route path="view" element={<TaskViewer />} />
        <Route path="generate" element={<Generator />} />
        <Route path="help" element={<Help />} />
      </Route>
    </Routes>
  );
}
