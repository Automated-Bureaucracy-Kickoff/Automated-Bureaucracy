import { motion } from "framer-motion";

export default function ContactSection() {
  const handleContact = () => {
    window.location.href = "mailto:blakedehaas@automatedbureaucracy.com";
  };

  return (
    <section id="contact" className="py-20 bg-gradient-to-r from-blue-600 to-purple-600 min-h-[30vh]">
      <div className="container mx-auto px-4">
        <div className="text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-8 text-white">
            Ready to Transform Your Organization?
          </h2>
          <p className="text-xl mb-12 max-w-2xl mx-auto text-gray-200">
            Join us in revolutionizing your workflow with cutting-edge AI solutions.
          </p>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleContact}
            className="w-3xs bg-blue-500 text-white px-6 py-3 rounded-full text-lg font-semibold hover:bg-blue-600 transition-all"
          >
            Contact Us
          </motion.button>
        </div>
      </div>
    </section>
  );
}
