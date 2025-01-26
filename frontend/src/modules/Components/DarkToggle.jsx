import { useEffect, useState } from 'react';

const DarkToggle = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    // Check the user's theme preference on component mount
    const root = window.document.documentElement;
    const initialTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (initialTheme === 'dark' || (!initialTheme && prefersDark)) {
      root.classList.add('dark');
      setIsDarkMode(true);
    } else {
      root.classList.remove('dark');
      setIsDarkMode(false);
    }
  }, []);

  const toggleTheme = () => {
    const root = window.document.documentElement;
    if (isDarkMode) {
      root.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      root.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
    setIsDarkMode(!isDarkMode);
  };

  return (
    <>
        <button onClick={toggleTheme} className="rounded-full border-2" aria-label="Toggle Dark Mode">
            <div className="p-2 flex space-x-2">
                <h2>Switch Theme</h2>
                <h2>{isDarkMode ? '🌙' : '☀️'}</h2>
            </div>
        </button>
    </>
  );
};

export default DarkToggle;