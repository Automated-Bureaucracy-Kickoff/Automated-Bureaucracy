import { useSelector } from "react-redux";
import AiIcon from "./AIicon";
import EditIcon from '@mui/icons-material/Edit';
import { useRef, useState } from "react";
const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const [title,setTitle]=useState("CHAT 1")
  return (
    <div className="response-container bg-black p-0 m-0 min-w-96 min-h-64 overflow-x-hidden" >

      <div className="text-white text-3xl font-bold bg-black/30 p-4 mb-3 text-left z-20 fixed" style={{width:"100%"}}>
        {title||"Default Title"} <EditIcon className="relative -left-3 top-2" style={{height:"20px"}} onClick={()=>{let text = prompt("enter yor title"); setTitle(text)}}/>
      </div>

      {messages.map((ele, index) => (
        <>
          <div
            className={`message ${index % 2 == 0 ? "message-right" : "message-left"} min-w-56 dark:bg-zinc-700 mb-16 min-h-fit relative `}
            key={index+ele[0]}
          >
            {index % 2 != 0 ? <AiIcon /> : ""}
            {ele[0]}
            <br />
            <h1 className="text-right"> {ele[1]} </h1>
          </div>

        </>
      ))}

    </div>
  );
};

export default Response;
