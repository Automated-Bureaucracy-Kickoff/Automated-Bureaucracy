import { useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { aiResponse, setflag, userQuery } from "../redux/slices/chatbotState"
import SendIcon from '@mui/icons-material/Send';
import mimickApi from "../controller/api-Mimick";
import FileUpload from "./FileUpload";
const Input = () => {
    const dispatch = useDispatch()
    let flag = useSelector((state) => state.chatbot.flag)
    const chatbot = useRef()
    const sendChat = async () => {
        if (flag) {
            let message = chatbot.current.value
            dispatch(setflag({flag:false}))
            chatbot.current.value=""
            dispatch(userQuery({ message:[message,new Date().toLocaleString([],{ hour: '2-digit', minute: '2-digit' })] }))
            dispatch(aiResponse({ message: ["Thinking......",new Date().toLocaleString([],{ hour: '2-digit', minute: '2-digit' })] }))
            try{
                const data = await mimickApi(message)
                dispatch(aiResponse({ message: JSON.parse(data).message }))
            }catch(err){
                dispatch(aiResponse({ message: err }))
            }
            dispatch(setflag({flag:true}))
        }
    }

    return (
        <div className="chat-container min-w-80" >
            <textarea  onKeyDown={(event)=>{if(event.key=="Enter"  && !event.shiftKey)sendChat()}} className="chat-input dark:bg-zinc-700 min-w-48 " placeholder="Type here..." ref={chatbot} type="text" />
             <FileUpload/>
             <SendIcon className=" relative -left-6" onClick={sendChat}  />
             
        </div>

    )
}

export default Input