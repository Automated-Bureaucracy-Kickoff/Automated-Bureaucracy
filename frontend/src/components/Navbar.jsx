import { useState } from "react";
import { Link } from "react-router-dom";
import { Menu, Close } from "@mui/icons-material";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import AccountBoxIcon from '@mui/icons-material/AccountBox';
import DarkToggle from "./DarkToggle";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };


  return (
    <nav className="w-full h-16 z-10  text-black  dark:text-zinc-200">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        {/* Logo */}
        <div className="text-xl font-bold">
          <Link to="/">
            <div className="flex items-center space-x-2">
              <h1>Automated Bureaucracy</h1>
            </div>
          </Link>
        </div>

        {/* Hamburger Icon (Visible on small screens) */}
        <button
          className="md:hidden block text-black dark:text-white focus:outline-none"
          onClick={toggleMenu}
          aria-label="Toggle Menu"
        >
          {isMenuOpen ? (
            <Close fontSize="large" />
          ) : (
            <Menu fontSize="large" />
          )}
        </button>

        {/* Links for Desktop */}
        <ul className="hidden md:flex items-center space-x-6">
            <li>
                <DarkToggle></DarkToggle>
            </li>
            
        </ul>

        {/* Mobile Menu (Visible when menu icon is clicked) */}
        {isMenuOpen && (
          <ul className="md:hidden sticky top-0 w-full bg-zinc-200 dark:bg-zinc-800 flex flex-col space-y-4 p-4 shadow-lg">
         
                <li>
                    <Link 
                        to="/account" 
                        className="text-gray-700 dark:text-gray-200 hover:text-gray-500 dark:hover:text-gray-400"
                    >
                        <AccountBoxIcon fontSize="large" />
                    </Link>
                </li>
                <li>
                    <DarkToggle></DarkToggle>
                </li>
          </ul>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
