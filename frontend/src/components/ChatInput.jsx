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
      dispatch(setflag({ flag: false }))
      chatbot.current.value = ""
      dispatch(userQuery({ message: [message, new Date().toLocaleString([], { hour: '2-digit', minute: '2-digit' })] }))
      dispatch(aiResponse({ message: ["Thinking......", new Date().toLocaleString([], { hour: '2-digit', minute: '2-digit' })] }))
      try {
        const data = await mimickApi({ message, settings })
        dispatch(aiResponse({ message: JSON.parse(data).message, ...settings }))
      } catch (err) {
        dispatch(aiResponse({ message: JSON.parse(err).message }))
      }
      dispatch(setflag({ flag: true }))
    }
  }

  return (
    <div className="relative -top-16 -left-16 flex flex-row items-center justify-center mx-auto w-3/4 h-full p-2 space-x-2">

        {/* Textarea for Chat */}
        <textarea
            onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) sendChat();
            }}
            className="flex-1 rounded-lg p-2 border border-[var(--color-tertiary-bg)] dark:border-[var(--color-tertiary-bg)] outline-none transition duration-300 focus:border-blue-500 text-[var(--color-primary-text)] dark:text-[var(--color-primary-text-dark)] bg-[var(--color-secondary-bg)] dark:bg-[var(--color-secondary-bg)] resize-none box-border"
            placeholder="Type here..."
            ref={chatbot}
            type="text"
        />
         {/* <div className="loading lv-circles sm lvl-5" data-label="Loading..." style={{display:"none"}}></div> */}
        {/* File Upload Button */}
        <FileUpload />
        <SendIcon onClick={sendChat}/>

      
    </div>
  );

}

export default Input