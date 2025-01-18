import { useState } from 'react'
import './App.css'
import ChatBot from './modules/Chatbot/pages/ChatBot'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <ChatBot/>

    </>
  )
}

export default App
