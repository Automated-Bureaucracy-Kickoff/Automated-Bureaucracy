import Response from "./ChatResponse"
import Input from "./ChatInput"

const ChatBot = () => {

    return (

        <div className="bg-primary-bg-light dark:bg-primary-bg-dark p-0 m-0 min-w-full overflow-hidden ">
        <Response />
        <Input />
        </div>
    )

}


export default ChatBot