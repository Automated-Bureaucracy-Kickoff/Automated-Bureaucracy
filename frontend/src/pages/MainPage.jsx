import { useSelector, useDispatch } from "react-redux"
import { motion, AnimatePresence } from "framer-motion"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"
import ChatSetup from "../components/ChatSetup"
import { useEffect, useState } from "react"
import { useLocation } from "react-router-dom"
import ParticlesComponent from "../components/Particle"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { appendHistory } from "../redux/slices/previousChat"
import { clearChat, updateTitle } from "../redux/slices/chatbotState"

const MainPage = () => {
    const settingToggle = useSelector((state) => state.toggle.settingsDisplay)
    const [isHistoryOpen, setIsHistoryOpen] = useState(window.innerWidth >= 768)
    const [showSetup, setShowSetup] = useState(false)
    const dispatch = useDispatch()
    let location = useLocation()   

    useEffect(() => {
        if(location.pathname === "/main") {
            document.querySelector(".overflowremover").style.overflowY = "hidden"
        }

        const handleResize = () => {
            setIsHistoryOpen(window.innerWidth >= 768)
        }

        window.addEventListener('resize', handleResize)
        return () => window.removeEventListener('resize', handleResize)
    }, [])

    const handleSetupComplete = (config) => {
        // Save the new chat to history
        dispatch(appendHistory(config));
        
        // Update current chat state
        dispatch(clearChat());
        dispatch(updateTitle({ title: config.chatName }));
        
        // Close setup and history window
        setShowSetup(false);
        setIsHistoryOpen(false);
    };

    const handleHistoryToggle = (open) => {
        setIsHistoryOpen(open);
    };

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="relative w-full h-full"
        >
            <ParticlesComponent id="main-particles" />
            
            <div className="flex w-full h-full bg-gradient-to-b from-gray-900/90 to-gray-800/90 dark:from-gray-900/90 dark:to-gray-800/90">
                <AnimatePresence mode="wait">
                    {isHistoryOpen && (
                        <motion.div 
                            initial={{ x: -300, opacity: 0 }}
                            animate={{ x: 0, opacity: 1 }}
                            exit={{ x: -300, opacity: 0 }}
                            transition={{ duration: 0.3 }}
                            className="absolute md:relative h-full w-[300px] z-20"
                        >
                            <HistorySection onNewChat={() => setShowSetup(true)} />
                        </motion.div>
                    )}
                </AnimatePresence>
                
                <motion.button
                    onClick={() => setIsHistoryOpen(!isHistoryOpen)}
                    className="absolute left-0 top-1/2 -translate-y-1/2 z-30 
                             bg-gray-800/80 hover:bg-gray-700/80 
                             text-white p-2 rounded-r-lg
                             backdrop-blur-sm transition-colors"
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                >
                    {isHistoryOpen ? <ChevronLeft /> : <ChevronRight />}
                </motion.button>
                
                <motion.div 
                    initial={{ x: 50, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: 0.3 }}
                    className="flex w-full h-full rounded-lg backdrop-blur-sm"
                >
                    {showSetup ? (
                        <ChatSetup 
                            onComplete={handleSetupComplete} 
                            onCancel={() => setShowSetup(false)} 
                        />
                    ) : (
                        settingToggle ? <Settings /> : <ChatBot onOpenHistory={() => handleHistoryToggle(true)} />
                    )}
                </motion.div>
            </div>
        </motion.div>
    )
}

export default MainPage