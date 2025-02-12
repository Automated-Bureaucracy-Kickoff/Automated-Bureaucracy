import { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronRight, ChevronLeft, ChevronDown } from 'lucide-react';
import { useDispatch } from "react-redux";
import { clearChat, updateTitle } from "../redux/slices/chatbotState";
import { appendHistory } from "../redux/slices/previousChat";

// Step 1: Chat Settings
const ChatSettings = ({ onNext, onBack, initialData }) => {
  const [chatName, setChatName] = useState(initialData?.chatName || 'New Chat');
  const [numAgents, setNumAgents] = useState(initialData?.numAgents || 2);
  const [numInteractions, setNumInteractions] = useState(initialData?.numInteractions || 3);

  return (
    <motion.div
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -50 }}
      className="w-full max-w-2xl mx-auto p-6 space-y-8"
    >
      <div className="space-y-4">
        <h2 className="text-2xl font-bold text-white text-center">
          Chat Setup
        </h2>
        <div className="flex justify-between items-center">
          <button
            onClick={onBack}
            className="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors flex items-center space-x-2"
          >
            <ChevronLeft size={20} />
            <span>Back</span>
          </button>
          <button
            onClick={() => onNext({ chatName, numAgents, numInteractions })}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors flex items-center space-x-2"
          >
            <span>Next</span>
            <ChevronRight size={20} />
          </button>
        </div>
      </div>
      
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-white mb-2">Chat Name</label>
          <input
            type="text"
            value={chatName}
            onChange={(e) => setChatName(e.target.value)}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-white mb-2">Number of Agents</label>
          <input
            type="number"
            min="2"
            max="5"
            value={numAgents}
            onChange={(e) => setNumAgents(Number(e.target.value))}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
          />
          <p className="text-gray-400 text-sm mt-1">Min: 2, Max: 5 agents</p>
        </div>

        <div>
          <label className="block text-sm font-medium text-white mb-2">
            Interactions per Prompt
          </label>
          <input
            type="number"
            min="1"
            max="10"
            value={numInteractions}
            onChange={(e) => setNumInteractions(Number(e.target.value))}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
          />
          <p className="text-gray-400 text-sm mt-1">Min: 1, Max: 10 interactions</p>
        </div>
      </div>
    </motion.div>
  );
};

// Step 2: Agent Configuration
const AgentSetup = ({ agentIndex, totalAgents, onNext, onBack, onComplete, initialData }) => {
  const [config, setConfig] = useState({
    name: initialData?.name || `Agent ${agentIndex + 1}`,
    systemPrompt: initialData?.systemPrompt || '',
    model: initialData?.model || 'gpt-3.5-turbo',
    tools: initialData?.tools || {
      webSearch: false,
      codeInterpreter: false,
      fileAccess: false,
      imageGeneration: false
    }
  });

  const [showToolsDropdown, setShowToolsDropdown] = useState(false);
  const [showError, setShowError] = useState(false);
  const dropdownRef = useRef(null);

  const models = [
    'gpt-3.5-turbo',
    'gpt-4',
    'claude-3-opus',
    'claude-3-sonnet',
    'gemini-pro'
  ];

  const toolLabels = {
    webSearch: 'Web Search',
    codeInterpreter: 'Code Interpreter',
    fileAccess: 'File Access',
    imageGeneration: 'Image Generation'
  };

  const handleNext = () => {
    if (!config.systemPrompt.trim()) {
      setShowError(true);
      setTimeout(() => setShowError(false), 3000);
      return;
    }

    if (agentIndex === totalAgents - 1) {
      onComplete(config);
    } else {
      onNext(config);
    }
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setShowToolsDropdown(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -50 }}
      className="w-full max-w-2xl mx-auto p-6 space-y-8"
    >
      <div className="space-y-4">
        <h2 className="text-2xl font-bold text-white text-center">
          Configure Agent {agentIndex + 1} of {totalAgents}
        </h2>
        <div className="flex justify-between items-center">
          <button
            onClick={onBack}
            className="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors flex items-center space-x-2"
          >
            <ChevronLeft size={20} />
            <span>Back</span>
          </button>
          <button
            onClick={handleNext}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors flex items-center space-x-2"
          >
            <span>{agentIndex === totalAgents - 1 ? 'Save' : 'Next'}</span>
            <ChevronRight size={20} />
          </button>
        </div>
      </div>

      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-white mb-2">Agent Name</label>
          <input
            type="text"
            value={config.name}
            onChange={(e) => setConfig({ ...config, name: e.target.value })}
            placeholder={`Agent ${agentIndex + 1}`}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-white mb-2">
            System Prompt
            {showError && (
              <motion.span
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="ml-2 text-red-500"
              >
                Complete system prompt before continuing
              </motion.span>
            )}
          </label>
          <textarea
            value={config.systemPrompt}
            onChange={(e) => setConfig({ ...config, systemPrompt: e.target.value })}
            className={`w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 
                       outline-none transition-all duration-200
                       ${showError ? 'ring-2 ring-red-500' : 'focus:ring-blue-500'}`}
            rows={4}
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-white mb-2">Model</label>
          <select
            value={config.model}
            onChange={(e) => setConfig({ ...config, model: e.target.value })}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
          >
            {models.map((model) => (
              <option key={model} value={model}>{model}</option>
            ))}
          </select>
        </div>

        <div className="relative" ref={dropdownRef}>
          <label className="block text-sm font-medium text-white mb-2">Tools</label>
          <button
            onClick={() => setShowToolsDropdown(!showToolsDropdown)}
            className="w-full bg-gray-700 text-white rounded-lg px-4 py-2 flex justify-between items-center hover:bg-gray-600 transition-colors"
          >
            <span>
              {Object.entries(config.tools).filter(([_, enabled]) => enabled).length} tools selected
            </span>
            <ChevronDown 
              className={`transform transition-transform ${showToolsDropdown ? 'rotate-180' : ''}`}
            />
          </button>
          
          <AnimatePresence>
            {showToolsDropdown && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="absolute z-50 w-full mt-2 bg-gray-700 rounded-lg shadow-lg border border-gray-600"
              >
                {Object.entries(config.tools).map(([tool, enabled]) => (
                  <label
                    key={tool}
                    className="flex items-center space-x-2 px-4 py-2 hover:bg-gray-600 cursor-pointer"
                  >
                    <input
                      type="checkbox"
                      checked={enabled}
                      onChange={(e) => setConfig({
                        ...config,
                        tools: { ...config.tools, [tool]: e.target.checked }
                      })}
                      className="rounded border-gray-400 text-blue-600 focus:ring-blue-500"
                    />
                    <span className="text-white">{toolLabels[tool]}</span>
                  </label>
                ))}
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>
    </motion.div>
  );
};

// Main ChatSetup Component
function ChatSetup({ onComplete, onCancel }) {
  const [step, setStep] = useState(0);
  const [chatSettings, setChatSettings] = useState(null);
  const [agentConfigs, setAgentConfigs] = useState([]);
  const dispatch = useDispatch();

  const handleChatSettingsComplete = (settings) => {
    setChatSettings(settings);
    setStep(1);
  };

  const handleAgentSetup = (config) => {
    const newConfigs = [...agentConfigs, config];
    setAgentConfigs(newConfigs);
    
    if (newConfigs.length === chatSettings.numAgents) {
      const configSummary = `Chat Configuration:\n` +
        `• Number of Agents: ${chatSettings.numAgents}\n` +
        `• Number of Interactions: ${chatSettings.numInteractions}\n` +
        `• Agents:\n${newConfigs.map((agent, i) => 
          `  ${i + 1}. ${agent.name}: ${agent.role}`
        ).join('\n')}`;

      const completeChatConfig = {
        messages: [["system", configSummary]],
        title: chatSettings.chatName,
        files: [],
        agents: newConfigs,
        numInteractions: chatSettings.numInteractions,
        timestamp: new Date().toISOString()
      };
      
      // Update current chat state
      dispatch(clearChat());
      dispatch(updateTitle({ title: completeChatConfig.title }));
      
      // Save to history
      dispatch(appendHistory(completeChatConfig));
      
      // Complete setup and close the setup window
      onComplete(completeChatConfig);
    }
  };

  const handleBack = () => {
    if (step === 1) {
      setStep(0);
      setAgentConfigs([]);
    } else {
      onCancel(); // Return to chat history
    }
  };

  return (
    <div className="w-full h-full bg-gray-800/90 backdrop-blur-sm overflow-y-auto">
      <AnimatePresence mode="wait">
        {step === 0 ? (
          <ChatSettings
            key="chat-settings"
            onNext={handleChatSettingsComplete}
            onBack={handleBack}
            initialData={chatSettings}
          />
        ) : (
          <AgentSetup
            key={`agent-${agentConfigs.length}`}
            agentIndex={agentConfigs.length}
            totalAgents={chatSettings.numAgents}
            onNext={handleAgentSetup}
            onBack={handleBack}
            onComplete={handleAgentSetup}
            initialData={agentConfigs[agentConfigs.length]}
          />
        )}
      </AnimatePresence>
    </div>
  );
}

export default ChatSetup; 