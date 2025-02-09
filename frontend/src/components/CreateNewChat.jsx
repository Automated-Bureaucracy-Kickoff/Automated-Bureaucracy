import { useDispatch, useSelector } from "react-redux";
import { createHistory } from "../redux/slices/chatbotState";
import { toggleSetting } from "../redux/slices/settings";
import { appendHistory } from "../redux/slices/previousChat";
function CreateNewChat() {
    const dispatch = useDispatch()
    const { messages, files, title } = useSelector((state) => state.chatbot)
    function clearChat() {
        dispatch(createHistory())
        dispatch(appendHistory({ messages, files, title }))
    }
    return (
        <div className="flex w-full h-16 justify-evenly relative " >
           
            <button
                onClick={clearChat}
                className=" capitalize 
                            font-bold     
                            text-[var(--color-primary-text)] 
                            dark:text-[var(--color-primary-text)] 
                            bg-[var(--color-primary-bg)] 
                            dark:bg-[var(--color-primary-bg)] 
                            hover:bg-[var(--color-secondary-bg)] 
                            dark:hover:bg-[var(--color-secondary-bg)]
                            absolute
                            top-[40px] right-1
                            "
            >
                Create New Chat
            </button>


        </div>
    )
}

export default CreateNewChat