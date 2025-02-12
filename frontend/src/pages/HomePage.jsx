import React from 'react';
import { motion } from 'framer-motion';
import { Brain, Bot, Workflow, Building2, Users, BarChart as ChartBar } from 'lucide-react';
import FadeInWhenVisible from '../components/FadeIn';
import HeroSection from '../components/Header';
import ContactSection from '../components/Contact';
import { useNavigate } from 'react-router-dom';

function LandingPage() {
  const navigate = useNavigate();

  const handleLearnMore = () => {
    navigate('/aboutus');
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white">
      {/* Hero Section */}
      <HeroSection/>

      
      <section id='services' className="py-20 bg-gray-800/50">
        <div className="container mx-auto px-4">
          <FadeInWhenVisible>
            <h2 className="text-3xl md:text-4xl font-bold text-center mb-16">Our Services</h2>
          </FadeInWhenVisible>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              {
                icon: <Brain className="w-12 h-12 text-blue-400" />,
                title: "AI Consulting",
                description: "Expert guidance on implementing AI solutions tailored to your organization's needs"
              },
              {
                icon: <Bot className="w-12 h-12 text-purple-400" />,
                title: "Multi-Agent Systems",
                description: "Advanced automation systems using multiple AI agents working in harmony"
              },
              {
                icon: <Workflow className="w-12 h-12 text-green-400" />,
                title: "Custom Workflows",
                description: "Streamlined processes designed specifically for your business requirements"
              },
              {
                icon: <Building2 className="w-12 h-12 text-yellow-400" />,
                title: "Enterprise Solutions",
                description: "Scalable automation solutions for organizations of all sizes"
              },
              {
                icon: <Users className="w-12 h-12 text-red-400" />,
                title: "Collective Success",
                description: "Co-owned success model ensuring aligned interests and optimal outcomes"
              },
              {
                icon: <ChartBar className="w-12 h-12 text-indigo-400" />,
                title: "Market Insights",
                description: "Data-driven analysis and certified reviews of automation technologies"
              }
            ].map((feature, index) => (
              <FadeInWhenVisible key={index}>
                <div className="bg-gray-700/50 p-8 rounded-xl hover:bg-gray-700/70 transition-colors">
                  <div className="mb-4">{feature.icon}</div>
                  <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
                  <p className="text-gray-300">{feature.description}</p>
                </div>
              </FadeInWhenVisible>
            ))}
          </div>
        </div>
      </section>

      {/* Vision*/}
      <section   className="py-20 ">
        <div id='about' className="container mx-auto px-4">
          <FadeInWhenVisible>
            <div className="max-w-4xl mx-auto text-center">
              <h2 className="text-3xl md:text-4xl font-bold mb-8">Our Vision</h2>
              <p className="text-lg text-gray-300 mb-8">
                We are an automation and Agentic AI consulting collective that co-owns its success, 
                dedicated to delivering cutting-edge multi-agent automation solutions and expert market 
                insights to NGOs, public, and private sector partners through certified reviews, 
                custom-built workflows, and fully maintained AI-driven systems.
              </p>
              <div className="relative inline-block">
                <motion.button
                  onClick={handleLearnMore}
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.95 }}
                  style={{ 
                    position: 'relative',
                    zIndex: 50,
                    cursor: 'pointer'
                  }}
                  className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-full text-lg font-semibold transition-all shadow-lg pointer-events-auto"
                >
                  Learn More
                </motion.button>
              </div>
            </div>
          </FadeInWhenVisible>
        </div>
      </section>

      {/* CTA Section */}
      <ContactSection/>

    </div>
  );
}

export default LandingPage;