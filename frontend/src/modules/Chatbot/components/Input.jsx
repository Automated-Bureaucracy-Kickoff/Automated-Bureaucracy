import { useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { aiResponse, setflag, userQuery } from "../../../store/slices/chatbotState"
import AI from "../../../controller/api-AI"

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
        <div className="flex border-4 p-2 m-4 rounded-lg w-fit space-x-4">
            <input className="" placeholder="Type here..." ref={chatbot} type="text" />
            <img onClick={sendChat} className="p-2 border-2 rounded-full" src="/sendIcon.png" alt="Send" />
        </div>

    )
}

export default Input