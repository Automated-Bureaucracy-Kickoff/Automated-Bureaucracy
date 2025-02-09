import { useState } from "react";
import { motion } from "framer-motion";

export default function ContactSection() {
  const [formData, setFormData] = useState({ name: "", email: "" });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form Submitted:", formData);
    // Handle form submission logic (e.g., send data to backend)
  };

  return (
    <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-600 min-h-[30vh]">
      <div className="container mx-auto px-4">
        <div className="text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-8 text-white">
            Ready to Transform Your Organization?
          </h2>
          <p className="text-xl mb-12 max-w-2xl mx-auto text-gray-200">
            Join us in revolutionizing your workflow with cutting-edge AI solutions.
          </p>
          <form 
            onSubmit={handleSubmit} 
            className="bg-white/10 backdrop-blur-lg p-6 rounded-lg shadow-lg max-w-md mx-auto min-h-[50vh] flex  items-center flex-col mt-10               "
          >
             <h1 className="text-4xl font-bold    "    >    Contact Us </h1>
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              defaultValue=""
              onChange={handleChange}
              required
              className="w-full p-3 border border-gray-400 rounded-md mb-4 bg-transparent text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 mt-10"
            />
            <input
              type="email"
              name="email"
              placeholder="Your Email"
              defaultValue=""
              onChange={handleChange}
              required
              className="w-full p-3 border border-gray-400 rounded-md mb-4 bg-transparent text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              type="submit"
              className="w-3xs bg-blue-500 text-white px-6 py-3 rounded-full text-lg font-semibold hover:bg-blue-600 transition-all mt-10"
            >
              Submit
            </motion.button>
          </form>
        </div>
      </div>
    </section>
  );
}
