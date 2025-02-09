import { Link } from 'react-router-dom';
import { HashLink } from 'react-router-hash-link';


function LandingNavbar() {

  return (
    <nav className="absolute z-40 top-14 left-0 right-0 mx-auto max-w-2xl px-4 rounded-[12px]">
      <div className="bg-[#192333] backdrop-blur-sm rounded-lg shadow-lg px-6 py-4">
        <div className="flex  justify-center ">
          {/* Desktop menu */}
          <div className="flex items-center space-x-8">
            <a 
              href="#about" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              Company's Vision
            </a>
            <a 
              href="#services" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              Services
            </a>
            <a 
              href="#contact" 
              className="text-[#E2E8F0] hover:text-[#4169E1] transition-colors duration-200"
            >
              Contact
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default LandingNavbar;