import { useState } from "react";
import { Link } from "react-router-dom";
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
              <h1 className="md:text-3xl">Automated Bureaucracy</h1>
            </div>
          </Link>
        </div>


        {/* Links for Desktop */}
        <ul className="flex items-center space-x-6">
            <li>
                <DarkToggle></DarkToggle>
            </li>
            
        </ul>

      </div>
    </nav>
  );
};

export default Navbar;
