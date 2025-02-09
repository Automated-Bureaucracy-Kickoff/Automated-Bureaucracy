import React from "react";
import { motion } from "framer-motion";
import ParticlesComponent from "./Particle";
import { useNavigate } from "react-router-dom";

 function Header() {
    const navigate = useNavigate()
  return (
    <header className="container mx-auto px-4 py-16 md:py-32 h-[100vh] grid place-items-center ">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="text-center"
      >
        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
          whileHover={{ scale: 1.05 }}
          className="text-4xl md:text-6xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600 z-20"
        >
          Automated Bureaucracy
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1.2, delay: 0.3 }}
          className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto mb-12"
        >
          Transforming organizations with cutting-edge multi-agent automation
          solutions and AI-driven workflows
        </motion.p>

        <motion.button
          whileHover={{ scale: 1.1, backgroundColor: "#4f46e5" }}
          whileTap={{ scale: 0.95 }}
          className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-full text-lg font-semibold transition-all shadow-lg"
          onClick={() => navigate("/main")}
        >
          Get Started
        </motion.button>
      </motion.div>
     
    </header>
  );
}

export default function HeroSection() {
    return (
      <div className="relative w-full h-screen">
      
        <ParticlesComponent id="particles" />
  
        <div className="absolute inset-0 z-10">
          <Header />
        </div>
      </div>
    );
  }

