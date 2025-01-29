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
        <div style={{ marginTop: "10px", padding: "2px" }}>
            <Button onClick={clearChat} style={{ position: "absolute", top: "85px", color: "whitesmoke", textTransform: "capitalize", left: "17vh" }}>Create new Chat <AddIcon className="animate-pulse" /> </Button>
            <SettingsIcon onClick={() => dispatch(toggleSetting())} className="hover:animate-spin" style={{ position: "absolute", top: "90px", left: "12px" }} />
        </div>
    )
}

export default CreateNewChat