import React from 'react';
import { motion } from 'framer-motion';
import ParticlesComponent from '../components/Particle';
import { LinkedIn, Email } from '@mui/icons-material';

const teamMembers = [
  {
    name: "Blake DeHaas",
    title: "Founder & CEO",
    bio: "Expert in multi-agent collective intelligence systems with a research focus on AI Safety & Alignment.",
    image: "/profilepic_blakedehaas.png",
    linkedin: "https://linkedin.com/in/blakedehaas",
    email: "blakedehaas@automatedbureaucracy.com"
  },
  {
    name: "Sathish Kumar",
    title: "Chief Machine Learning Officer",
    bio: "Machine Learning Engineer Specializing in AI Pipelines, MLOps, and Scalable Solutions.",
    image: "/profilepic_sathishkumar.png",
    linkedin: "https://www.linkedin.com/in/sathishkumarai/",
  },
  {
    name: "Noah Vilas",
    title: "Chief Operations Officer",
    bio: "Jack of all trades when it comes to CS, experience in everything from making my own computer from logic gates to implementing deep learning for personal and academic projects.",
    image: "/profilepic_noahvilas.png",
    linkedin: "https://www.linkedin.com/in/noah-vilas/",
  },
  {
    name: "Brady Golomb",
    title: "Chief Systems Engineer",
    bio: "Aerospace Engineer with experience in Mission Operations, focused on building maintainable and scalable codebases.",
    image: "/profilepic_bradygolomb.png",
    linkedin: "https://www.linkedin.com/in/brady-golomb/",
  },
  {
    name: "Lakshay Jain",
    title: "Chief Frontend Engineer",
    bio: "Frontend developer experienced in Node.js, Express.js, React js and Vite to build engaging user experiences through frontend implementation.",
    image: "/profilepic_lakshayjain.png",
    linkedin: "https://www.linkedin.com/in/lakshay-jain-1307532a1/",
    email:"lakshaybusiness.12@gmail.com"
  },
  {
    name: "Ananya Pandey",
    title: "Chief Mobile Developer",
    bio: "Focused on Android development for mobile applications with a deep passion for programming.",
    image: "/profilepic_ananyapandey.png",
    linkedin: "https://www.linkedin.com/in/ananya-pandey-b45864295/",
  }
];

export default function AboutUsPage() {
  return (
    <div className="relative min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white">
      <ParticlesComponent id="particles" />
      
      <div className="relative z-10 container mx-auto px-4 pt-32 pb-20">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-4xl md:text-6xl font-bold text-center mb-16 relative z-20"
        >
          About Us
        </motion.h1>

        {/* Video Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
          {/* First Video */}
          <div className="flex flex-col">
            <h2 className="text-xl font-bold mb-4 text-center text-blue-400">
              Founder Introduction
            </h2>
            <div className="aspect-video">
              <iframe 
                className="w-full h-full rounded-lg"
                src="https://www.youtube.com/embed/fO3xOjDS2mY"
                title="Founder Introduction"
                allowFullScreen
              />
            </div>
          </div>

          {/* Second Video */}
          <div className="flex flex-col">
            <h2 className="text-xl font-bold mb-4 text-center text-blue-400">
              Multi-Agent Model Demo
            </h2>
            <div className="aspect-video">
              <iframe 
                className="w-full h-full rounded-lg"
                src="https://www.youtube.com/embed/bTaRu5qM0EU"
                title="Multi-Agent Model Demo"
                allowFullScreen
              />
            </div>
          </div>

          {/* Third Video */}
          <div className="flex flex-col">
            <h2 className="text-xl font-bold mb-4 text-center text-blue-400">
              Simulation Output Example
            </h2>
            <div className="aspect-video">
              <iframe 
                className="w-full h-full rounded-lg"
                src="https://www.youtube.com/embed/JAjfU1dqvfY"
                title="Simulation Output Example"
                allowFullScreen
              />
            </div>
          </div>
        </div>

        {/* Team Section */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        >
          {teamMembers.map((member, index) => (
            <motion.div
              key={member.name}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 * index }}
              className="bg-gray-800/50 rounded-lg p-6 hover:bg-gray-700/50 transition-colors"
            >
              <img 
                src={member.image} 
                alt={member.name}
                className="w-48 h-48 rounded-lg mx-auto mb-4 object-cover"
              />
              <h3 className="text-xl font-bold mb-2">{member.name}</h3>
              <p className="text-blue-400 mb-3">{member.title}</p>
              <p className="text-gray-300 mb-4">{member.bio}</p>
              <div className="flex justify-center space-x-4">
                <a href={member.linkedin} target="_blank" rel="noopener noreferrer">
                  <LinkedIn className="text-gray-300 hover:text-blue-400" />
                </a>
                {member.email && (
                  <a href={`mailto:${member.email}`}>
                    <Email className="text-gray-300 hover:text-blue-400" />
                  </a>
                )}
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  );
}