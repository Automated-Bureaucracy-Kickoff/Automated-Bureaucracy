import { useDispatch, useSelector } from "react-redux";
import AiIcon from "./AIicon";
import EditIcon from '@mui/icons-material/Edit';
import { createTitle } from "../redux/slices/chatbotState";
const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const dispatch = useDispatch()
  const title = useSelector((state)=>state.chatbot.title)
   
  return (
    <div className="flex flex-col w-full h-full p-5">
    <div className="text-[var(--color-primary-text)] text-3xl font-bold p-4 mb-3 text-left w-full">
        {title || "Default Title"}
        <EditIcon
        className="relative -left-1 top-1 cursor-pointer"
        style={{ height: "20px", color: "var(--color-secondary-text)" }}
        onClick={() => {
            const text = prompt("Enter your title");
            if (text) dispatch(createTitle(text));
        }}
        />
    </div>
    <div className="flex flex-col flex-1 overflow-y-auto">
  {messages.map((ele, index) => (
    <div
      key={index + ele[0]}
      className={`w-2/3 mb-2 p-3 rounded-lg text-xl break-words ${
        index % 2 === 0
          ? "self-end bg-[var(--color-message-left-bg)]"  // your message on left
          : "self-start bg-[var(--color-message-right-bg)]"   // response on right
      }`}
    >
      {index % 2 !== 0 && <AiIcon />}
      {ele[0]}
      <br />
      <br />
      <h1 className="text-right text-[var(--color-secondary-text)]">
        {ele[1]}
      </h1>
    </div>
  ))}
</div>

    </div>
  );
  
  
};

export default Response;
