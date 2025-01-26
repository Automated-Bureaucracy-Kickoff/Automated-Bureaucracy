import { useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { aiResponse, setflag, userQuery } from "../redux/slices/chatbotState"
import AI from "../controller/api-AI"

const Input = () => {
    const dispatch = useDispatch()
    let flag = useSelector((state) => state.chatbot.flag)
    const chatbot = useRef()
    const sendChat = async () => {
        if (flag) {
            let message = chatbot.current.value
            dispatch(setflag({flag:false}))
            chatbot.current.value=""
            dispatch(userQuery({ message }))
            dispatch(aiResponse({ message: "Thinking......" }))
            const data = await AI(message)
            dispatch(aiResponse({ message: JSON.parse(data).message }))
            dispatch(setflag({flag:true}))
        }
    }

    return (
        <div className="chat-container">
            <input className="chat-input" placeholder="Type here..." ref={chatbot} type="text" />
            <img onClick={sendChat} className="send-icon" src="/sendIcon.png" alt="Send" />
        </div>

    )
}

export default Input