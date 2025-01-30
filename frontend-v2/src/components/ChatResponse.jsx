import { useSelector } from "react-redux";
import AiIcon from "./AIicon";
import EditIcon from '@mui/icons-material/Edit';
import { useState } from "react";
const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const [title, setTitle] = useState("CHAT 1")
  return (
    <div className="response-container bg-primary-bg-light dark:bg-primary-bg-dark p-0 m-0 min-w-96 min-h-64 overflow-x-hidden" >

      <div className="text-primary-text-light dark:text-primary-text-dark text-3xl font-bold bg-tertiary-bg-light dark:bg-tertiary-bg-dark px-4 mb-3 text-left z-20 fixed">
        {title || "Default Title"} <EditIcon className="relative -left-3 top-1 bg-secondary-bg-light dark:bg-secondary-bg-dark" onClick={() => { let text = prompt("enter yor title"); setTitle(text) }} />
      </div>

      {messages.map((ele, index) => (
        <>
          <div
            className="min-w-56 bg-secondary-bg-light dark:bg-secondary-bg-dark mb-2 min-h-fit relative"
            key={index + ele[0]}
          >
            {index % 2 != 0 ? <>  <AiIcon /> </> : ""}
            {ele[0]}
            {index % 2 != 0 ? <>  <br /> <br /> </> : <><br /></>}
            <br />
            <h1 className="text-right"> {ele[1]} </h1>
          </div>

        </>
      ))}

    </div>
  );
};

export default Response;
