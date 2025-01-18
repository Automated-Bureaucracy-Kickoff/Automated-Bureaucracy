import { useRef } from "react"
import { useDispatch } from "react-redux"
import { aiResponse, userQuery } from "../../../store/slices/chatbotState"
import AI from "../../../controller/api-AI"

const Input = ()=>{
    const dispatch = useDispatch()
    const chatbot = useRef()
    const sendChat = async () => {
        dispatch(userQuery({message:chatbot.current.value}))
        const data = await AI(chatbot.current.value)
        dispatch(aiResponse({message:JSON.parse(data).message}))
        
    }

    return (
        <div className="chat-container">
        <input  className="chat-input" placeholder="Type here..." ref={chatbot} type="text" />
        <img onClick={sendChat} className="send-icon" src="/sendIcon.png" alt="Send" />
      </div>
      
    )
}

export default Input