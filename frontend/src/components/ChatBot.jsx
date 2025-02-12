import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import Response from "./ChatResponse";
import Input from "./ChatInput";
import { motion } from "framer-motion";

const ChatBot = ({ onOpenHistory }) => {
  const messages = useSelector((state) => state.chatbot.messages);
  const hasActiveChat = messages.length > 0;
  const dispatch = useDispatch();

  if (!hasActiveChat) {
    return (
      <div className="flex items-center justify-center h-full w-full">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center"
        >
          <h2 className="text-2xl font-semibold mb-4 text-gray-200">
            No Active Chat Selected
          </h2>
          <p className="text-gray-400 mb-6">
            Select an existing chat or configure a new one to get started
          </p>
          <motion.button
            onClick={onOpenHistory}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition-colors shadow-lg"
          >
            Open Chat History
          </motion.button>
        </motion.div>
      </div>
    );
  }

  return (
    <div className="relative w-full h-full">
      <div className="flex flex-col h-full w-full text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] rounded-[12px] justify-between -m-4">
        <div className="flex overflow-auto">
          <Response />
        </div>
        <div>
          <Input />
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
