import { useDispatch, useSelector } from "react-redux";
import { accessHistory, clearChat } from "../redux/slices/chatbotState";
import { removeHistory, clearAllHistory, appendHistory } from "../redux/slices/previousChat";
import { motion, AnimatePresence } from "framer-motion";
import { Plus, MessageSquare, Trash2, RefreshCw } from "lucide-react";
import ChatSetup from './ChatSetup';
import { useState } from 'react';
import { updateTitle } from '../redux/slices/chatbotState';

// Delete confirmation modal component
const DeleteConfirmModal = ({ isOpen, onClose, onConfirm, chatTitle }) => {
  if (!isOpen) return null;

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <motion.div
        initial={{ scale: 0.95 }}
        animate={{ scale: 1 }}
        exit={{ scale: 0.95 }}
        className="bg-gray-800 p-6 rounded-lg max-w-md w-full mx-4"
      >
        <h3 className="text-xl font-semibold text-white mb-4">Delete Chat</h3>
        <p className="text-gray-300 mb-6">
          Are you sure you want to delete "{chatTitle}"?
        </p>
        <div className="flex justify-end space-x-4">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg"
          >
            Cancel
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg"
          >
            Delete
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
};

function HistorySection({ onNewChat }) {
  const history = useSelector((state) => state.history.history);
  const currentChat = useSelector((state) => state.chatbot);
  const dispatch = useDispatch();
  const [showSetup, setShowSetup] = useState(false);
  const [deleteModal, setDeleteModal] = useState({ isOpen: false, chat: null });

  const createNewChat = () => {
    setShowSetup(true);
  };

  const handleSetupComplete = (config) => {
    // Create new chat with configuration
    dispatch(clearChat());
    dispatch(updateTitle({ title: config.chatName }));
    setShowSetup(false);
  };

  const handleClearAllHistory = () => {
    if (window.confirm("Are you sure you want to clear all chat history?")) {
      dispatch(clearAllHistory());
    }
  };

  const handleDeleteChat = (chat, e) => {
    e.stopPropagation();
    setDeleteModal({ isOpen: true, chat });
  };

  return (
    <div className="flex flex-col h-full w-full bg-gray-800/80 backdrop-blur-sm text-white p-4">
      <AnimatePresence>
        {deleteModal.isOpen && (
          <DeleteConfirmModal
            isOpen={deleteModal.isOpen}
            chatTitle={deleteModal.chat?.title}
            onClose={() => setDeleteModal({ isOpen: false, chat: null })}
            onConfirm={() => {
              dispatch(removeHistory({ title: deleteModal.chat.title }));
              setDeleteModal({ isOpen: false, chat: null });
            }}
          />
        )}
      </AnimatePresence>

      {showSetup ? (
        <ChatSetup onComplete={handleSetupComplete} onCancel={() => setShowSetup(false)} />
      ) : (
        <>
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-semibold">Chat History</h2>
            <div className="flex space-x-2">
              <motion.button
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
                onClick={createNewChat}
                className="p-2 bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors"
                aria-label="Create new chat"
              >
                <Plus size={20} />
              </motion.button>
              <motion.button
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
                onClick={handleClearAllHistory}
                className="p-2 bg-red-600 rounded-lg hover:bg-red-700 transition-colors"
                aria-label="Clear all history"
              >
                <RefreshCw size={20} />
              </motion.button>
            </div>
          </div>

          {/* Chat List */}
          <div className="flex-1 overflow-y-auto space-y-2">
            {/* Current Chat */}
            {currentChat.messages.length > 0 && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-blue-600/50 hover:bg-blue-600/70 
                         rounded-lg p-4 cursor-pointer transition-all
                         border border-blue-500"
              >
                <div className="flex items-center justify-between">
                  <div className="flex-1 min-w-0">
                    <h3 className="text-sm font-medium truncate">
                      {currentChat.title}
                    </h3>
                    <p className="text-xs text-gray-300">
                      {currentChat.messages.length} messages
                    </p>
                  </div>
                  <span className="text-xs bg-blue-500 px-2 py-1 rounded">
                    Current
                  </span>
                </div>
              </motion.div>
            )}

            {/* Previous Chats */}
            {history.length === 0 ? (
              <div className="text-center text-gray-400 mt-4">
                <MessageSquare className="mx-auto mb-2" size={24} />
                <p>No chat history yet</p>
              </div>
            ) : (
              history.map(({ title, messages, agents }, idx) => (
                <motion.div
                  key={title + idx}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: idx * 0.1 }}
                  className="group relative bg-gray-700 hover:bg-gray-600 
                             rounded-lg p-4 cursor-pointer transition-all
                             border border-transparent hover:border-blue-500"
                  onClick={() => {
                    // Only save current chat if it has messages and isn't already in history
                    if (currentChat.messages.length > 0 && !history.some(chat => chat.title === currentChat.title)) {
                      dispatch(appendHistory(currentChat));
                    }
                    dispatch(accessHistory({ 
                      messages: messages || [], 
                      title, 
                      files: [], 
                      agents: agents || [] 
                    }));
                  }}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex-1 min-w-0">
                      <h3 className="text-sm font-medium truncate">{title}</h3>
                      <p className="text-xs text-gray-400">
                        {messages?.length > 0 
                          ? `${messages.length} messages` 
                          : `${agents?.length || 0} agents configured`}
                      </p>
                    </div>
                    <motion.button
                      whileHover={{ scale: 1.1 }}
                      whileTap={{ scale: 0.9 }}
                      onClick={(e) => handleDeleteChat({ title }, e)}
                      className="opacity-0 group-hover:opacity-100 p-1 
                               hover:bg-red-500/20 rounded transition-all"
                      aria-label="Delete chat"
                    >
                      <Trash2 size={16} className="text-red-400" />
                    </motion.button>
                  </div>
                </motion.div>
              ))
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default HistorySection;

