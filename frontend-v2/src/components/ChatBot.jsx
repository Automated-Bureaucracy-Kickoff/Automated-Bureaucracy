import Response from "./ChatResponse"
import Input from "./ChatInput"
import "../css/ChatBot.css"

const ChatBot = () => {

    return (

        <div className="chatBotPage bg-black p-0 m-0 min-w-full overflow-hidden ">
        <Response />
        <Input />
        </div>
    )

}


export default ChatBot