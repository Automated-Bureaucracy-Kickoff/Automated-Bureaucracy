import { useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { aiResponse, setflag, userQuery } from "../redux/slices/chatbotState"
import SendIcon from '@mui/icons-material/Send';
import mimickApi from "../controller/api-Mimick";
import FileUpload from "./FileUpload";
const Input = () => {
    const dispatch = useDispatch()
    let flag = useSelector((state) => state.chatbot.flag)
    let settings = useSelector((state) => state.toggle.setting)
    const chatbot = useRef()
    const sendChat = async () => {
        if (flag) {
            let message = chatbot.current.value
            dispatch(setflag({flag:false}))
            chatbot.current.value=""
            dispatch(userQuery({ message:[message,new Date().toLocaleString([],{ hour: '2-digit', minute: '2-digit' })] }))
            dispatch(aiResponse({ message: ["Thinking......",new Date().toLocaleString([],{ hour: '2-digit', minute: '2-digit' })] }))
            try{
                const data = await mimickApi({message,settings})
                dispatch(aiResponse({ message: JSON.parse(data).message ,...settings}))
            }catch(err){
                dispatch(aiResponse({ message: JSON.parse(err).message }))
            }
            dispatch(setflag({flag:true}))
        }
    }

    return (
        <div className="chat-container min-w-80 relative" >
            <textarea  onKeyDown={(event)=>{if(event.key=="Enter"  && !event.shiftKey)sendChat()}} className="chat-input min-w-48  text-left pt-6 bg-gray-800 p-2 rounded border border-gray-700" placeholder="Type here..." ref={chatbot} type="text" />
             <FileUpload/>
             <SendIcon className=" relative -left-10 " onClick={sendChat}  />
             
        </div>

    )
}

export default Input