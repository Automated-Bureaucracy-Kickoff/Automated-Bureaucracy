import { useState, useRef } from "react";
import ChatBot from "../Chatbot/pages/ChatBot";
import DarkToggle from "../Components/DarkToggle";

const MainDashboard = () => {
  const [leftWidth, setLeftWidth] = useState(300); // Default width for the left column
  const draggerRef = useRef(null);

  const handleMouseDown = (e) => {
    const startX = e.clientX;
    const startLeftWidth = leftWidth;

    const handleMouseMove = (moveEvent) => {
      const deltaX = moveEvent.clientX - startX;
      setLeftWidth(Math.max(100, startLeftWidth + deltaX)); // Set min-width as 100px
    };

    const handleMouseUp = () => {
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
    };

    document.addEventListener("mousemove", handleMouseMove);
    document.addEventListener("mouseup", handleMouseUp);
  };

  return (
    <div className="flex flex-col h-full w-full">
      <div className="flex justify-between p-2 border-b-2 bg-zinc-200 dark:bg-zinc-700 dark:text-zinc-200">
        <h1 className="text-4xl">Automated Bureaucracy</h1>
        <DarkToggle />
      </div>
      <div className="flex flex-row h-full w-full">
        {/* Left Section */}
        <div
          className="min-w-96 flex flex-row justify-between"
          style={{ width: leftWidth }}
        >
          <img
            src="https://static-00.iconduck.com/assets.00/robot-icon-1936x2048-ajs789m0.png"
            className="w-16 h-16"
            alt="Robot"/>
            <img
            src="https://static-00.iconduck.com/assets.00/robot-icon-1936x2048-ajs789m0.png"
            className="w-16 h-16"
            alt="Robot"/>
            <img
            src="https://static-00.iconduck.com/assets.00/robot-icon-1936x2048-ajs789m0.png"
            className="w-16 h-16"
            alt="Robot"/>
        </div>

        {/* Resizer */}
        <div
          ref={draggerRef}
          className="cursor-col-resize bg-gray-400"
          style={{ width: "10px", height: "100%" }}
          onMouseDown={handleMouseDown}
        />

        {/* Right Section */}
        <div className="flex-grow">
          <ChatBot />
        </div>
      </div>
    </div>
  );
};

export default MainDashboard;