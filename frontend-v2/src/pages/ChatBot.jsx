import Response from "../components/ChatResponse"
import Input from "../components/ChatInput"
import "./Chatbot.css"

const ChatBot = () => {

    return (

        <div className="chatBotPage">
        <Response />
            <Input />
        </div>
    )

}


export default ChatBot