import { useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { aiResponse, setflag, userQuery } from "../redux/slices/chatbotState"
import SendIcon from '@mui/icons-material/Send';
import FileUpload from "./FileUpload";
import sendingDataToBackend from "../controller/api-backend";

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
        const { Analytica, Creativa, Pragmatica, Final_Analytica } = await sendingDataToBackend({ message, settings })
        const formattedMessage = `
### 🤖 **Analytica's Response**
> ${Analytica}

---

### 🎨 **Creativa's Response**
> ${Creativa}

---

### 🔧 **Pragmatica's Response**
> ${Pragmatica}

---

### 🏆 **Final Conclusion (Analytica)**
> ${Final_Analytica}
`;

        dispatch(aiResponse({ message: formattedMessage }));

      } catch (err) {
        dispatch(aiResponse({ message: JSON.parse(err).message }))
      }
      dispatch(setflag({ flag: true }))
    }
  }

  return (
    <div className="relative left-5  md:relative -top-10 md:-left-16 flex flex-row items-center justify-center mx-auto w-3/4 h-full p-2 space-x-2">
      {/* Textarea for Chat */}
      <textarea
        onKeyDown={(event) => {
          if (event.key === "Enter" && !event.shiftKey) sendChat();
        }}
        className="flex-1 rounded-lg p-2 border border-[var(--color-tertiary-bg)] dark:border-[var(--color-tertiary-bg)] outline-none transition duration-300 focus:border-blue-500 text-[var(--color-primary-text)] dark:text-[var(--color-primary-text-dark)] bg-[var(--color-secondary-bg)] dark:bg-[var(--color-secondary-bg)] resize-none box-border max-w-[70vw] min-h-[10vh] field-sizing-content scroll-auto max-h-[40vh] "
        placeholder="Type here..."
        ref={chatbot}
        type="text"
      />
      {/* <div className="loading lv-circles sm lvl-5" data-label="Loading..." style={{display:"none"}}></div> */}
      {/* File Upload Button */}
      <FileUpload />
      <SendIcon onClick={sendChat} />


    </div>
  );

}

export default Input