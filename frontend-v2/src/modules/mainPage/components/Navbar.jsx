// src/components/Navbar.jsx
import React from "react";

const Navbar = () => {
  return (
    <nav className="bg-blue-500 text-white">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        {/* Logo */}
        <div className="text-xl font-bold">
          <a href="/">MySite</a>
        </div>

        {/* Links */}
        <ul className="hidden md:flex space-x-6">
          <li>
            <a href="#home" className="hover:text-gray-300">
              Home
            </a>
          </li>
          <li>
            <a href="#about" className="hover:text-gray-300">
              About
            </a>
          </li>
          <li>
            <a href="#services" className="hover:text-gray-300">
              Services
            </a>
          </li>
          <li>
            <a href="#contact" className="hover:text-gray-300">
              Contact
            </a>
          </li>
        </ul>

        {/* Mobile Menu Button */}
        <button
          className="block md:hidden text-white hover:text-gray-300"
          aria-label="Toggle menu"
        >
          ☰
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
