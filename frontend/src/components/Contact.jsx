import { motion } from "framer-motion";
import { useState } from "react";

export default function ContactSection() {
  const [showMessage, setShowMessage] = useState(false);

  const handleContact = () => {
    console.log("Button clicked - attempting to open mailto"); // Debug log
    window.location.href = "mailto:blakedehaas@automatedbureaucracy.com";
    setShowMessage(true);
  };

  return (
    <section id="contact" className="py-20 bg-gradient-to-r from-blue-600 to-purple-600 min-h-[30vh] relative">
      <div className="container mx-auto px-4">
        <div className="text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-8 text-white">
            Ready to Transform Your Organization?
          </h2>
          <p className="text-xl mb-12 max-w-2xl mx-auto text-gray-200">
            Join us in revolutionizing your workflow with cutting-edge AI solutions.
          </p>
          <div className="relative inline-block">
            <motion.button
              onClick={handleContact}
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              style={{ 
                position: 'relative',
                zIndex: 50,
                cursor: 'pointer'
              }}
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-full text-lg font-semibold transition-all shadow-lg pointer-events-auto"
            >
              Contact Us
            </motion.button>
          </div>
          
          {showMessage && (
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              className="mt-6 text-gray-200 text-lg"
            >
              If your default mail client did not open automatically, email us directly at:{" "}
              <span className="font-semibold">blakedehaas@automatedbureaucracy.com</span>
            </motion.p>
          )}
        </div>
      </div>
    </section>
  );
}
