import { useDispatch, useSelector } from "react-redux";
import AiIcon from "./AIicon";
import EditIcon from '@mui/icons-material/Edit';
import { createTitle } from "../redux/slices/chatbotState";
const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const dispatch = useDispatch()
  const title = useSelector((state)=>state.chatbot.title)
   
  return (
    <div className="flex flex-col p-5">
    
      <div className="text-[var(--color-primary-text)] text-3xl font-bold p-4 mb-3 text-left z-20 fixed w-full">
        {title || "Default Title"} 
        <EditIcon
          className="relative -left-1 top-1"
          color="var(--color-secondary-text)"
          style={{ height: "20px" }}
          onClick={() => { 
            let text = prompt("Enter your title"); 
            dispatch(createTitle(text)); 
          }}
        />
      </div>
    
      {messages.map((ele, index) => (
        <div
        className={`${index % 2 === 0 ? "self-end bg-[var(--color-message-right-bg)]" : "self-start bg-[var(--color-message-left-bg)]"} 
                     dark:bg-[var(--color-secondary-bg-dark)] bg-[var(--color-secondary-bg)] 
                    mb-2 min-h-fit relative p-3 rounded-lg text-xl word-wrap break-words max-w-96 `}
            
        key={index + ele[0]}
      >
        {index % 2 !== 0 && <AiIcon />}
        {ele[0]}
        {index % 2 !== 0 ? <> <br /> <br /> </> : <><br /></>}
        <br />
        <h1 className="text-right text-[var(--color-secondary-text)]">{ele[1]}</h1>
      </div>
      
      ))}
    
    </div>
  );
  
  
};

export default Response;
