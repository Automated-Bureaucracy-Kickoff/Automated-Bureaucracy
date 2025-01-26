import { useState } from 'react'
import './App.css'
import ChatBot from './modules/Chatbot/pages/ChatBot'
import MainDashboard from './modules/pages/MainDashboard'

function App() {
    const [count, setCount] = useState(0)

    return (
        <>
            <div className="bg-zinc-100 dark:bg-zinc-800 w-screen h-screen">
                <MainDashboard/>
            </div>
        </>
    )
}

export default App
