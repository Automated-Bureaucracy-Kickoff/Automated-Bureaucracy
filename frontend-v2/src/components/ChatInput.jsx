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
    <div className="fixed bottom-[60px] right-[15vw] flex items-center 
                        rounded-[15px] ">

      <textarea
        onKeyDown={(event) => { if (event.key === "Enter" && !event.shiftKey) sendChat(); }}
        className="w-[40vw] h-[50px] rounded-[25px] px-5 text-[16px] 
             border border-[var(--color-tertiary-bg)] dark:border-[var(--color-tertiary-bg)] 
             outline-none transition duration-300 focus:border-blue-500 
             text-[var(--color-primary-text)] dark:text-[var(--color-primary-text-dark)] bg-[var(--color-secondary-bg)] dark:bg-[var(--color-secondary-bg)] resize-none box-border"
        placeholder="Type here..."
        ref={chatbot}
        type="text"
      />

      <FileUpload />

      <SendIcon
        className="w-[35px] cursor-pointer transition-transform duration-200 
                       hover:scale-110 text-[var(--color-primary-accent)] 
                       dark:text-[var(--color-primary-accent)] relative -left-9 "
        onClick={sendChat}
      />
    </div>
  );

}

export default Input