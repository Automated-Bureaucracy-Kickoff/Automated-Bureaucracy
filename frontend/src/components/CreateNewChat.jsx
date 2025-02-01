import { Button } from "@mui/material";
import AddIcon from '@mui/icons-material/Add';
import SettingsIcon from '@mui/icons-material/Settings';
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
        <div className="relative top-2 flex justify-evenly gap-8 " >
            <SettingsIcon className="m-2" onClick={() => dispatch(toggleSetting())} />
            <button
                onClick={clearChat}
                className=" capitalize 
                            font-bold     
                            text-[var(--color-primary-text)] 
                            dark:text-[var(--color-primary-text)] 
                            bg-[var(--color-primary-bg)] 
                            dark:bg-[var(--color-primary-bg)] 
                            hover:bg-[var(--color-secondary-bg)] 
                            dark:hover:bg-[var(--color-secondary-bg)]"
            >
                Create New Chat
            </button>


        </div>
    )
}

export default CreateNewChat