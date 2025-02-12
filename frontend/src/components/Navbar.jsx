import { useState } from "react";
import { Link } from "react-router-dom";
import DarkToggle from "./DarkToggle";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };


  return (
    <nav className="w-full h-16 z-10  text-black  dark:text-zinc-200 relative mt-3">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        {/* Logo */}
        <div className="text-xl font-bold absolute left-0">
          <Link to="/">
            <div className="flex items-center space-x-2">
              <h1 className="md:text-3xl">Automated Bureaucracy</h1>
            </div>
          </Link>
        </div>


        {/* Links for Desktop */}
        <ul className="flex items-center space-x-6 absolute right-[10px] ">
            <li>
                <DarkToggle></DarkToggle>
            </li>
            
        </ul>

      </div>
    </nav>
  );
};

function MainNavBar() {
  return (
    <nav className="absolute z-10 top-14 right-0 mx-auto w-1/2 px-4 rounded-[12px]">
      <div className="bg-[#192333]/80 backdrop-blur-sm rounded-lg shadow-lg px-6 py-4">
        <div className="flex justify-center">
          <div className="flex items-center space-x-8">
            <Link 
              to="/" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              Home
            </Link>
            <Link 
              to="/main" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              Multi-Agent Chat
            </Link>
            <Link 
              to="/aboutus" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              About Us
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
export { MainNavBar };