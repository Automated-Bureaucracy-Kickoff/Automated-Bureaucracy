import { useState, useEffect } from 'react';

function DarkToggle() {
  const [isDarkMode, setIsDarkMode] = useState(() => {
    // Load initial state from localStorage or default to light mode
    const savedMode = localStorage.getItem('darkMode') === 'true';
    if (savedMode) {
      document.documentElement.classList.add('dark');
    }
    return savedMode; // Initialize state based on saved value
  });

  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => {
      const newMode = !prevMode;
      if (newMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      return newMode;
    });
  };

  useEffect(() => {
    // Persist mode in localStorage
    localStorage.setItem('darkMode', isDarkMode);
  }, [isDarkMode]);

  return (
    <button
      onClick={toggleDarkMode}
      className="p-1 bg-zinc-600 rounded"
    >
      {isDarkMode ? '☀️' : '🌙'}
    </button>
  );
}

export default DarkToggle;
