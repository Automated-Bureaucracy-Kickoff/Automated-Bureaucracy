import { useEffect, useRef } from "react";
import { useSelector } from "react-redux";
import AiIcon from "./AIicon";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import { copyContent } from "../controller/api-copy";
import ReactMarkdown from "react-markdown";

const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const chatResponseRef = useRef(null);

  useEffect(() => {
    if (chatResponseRef.current) {
      chatResponseRef.current.scrollTo({
        top: chatResponseRef.current.scrollHeight+200,
        behavior: "smooth",
      });
    }
  }, [messages]);

  return (
    <>
      <div className="relative top-16 chatResponse overflow-y-auto flex flex-col w-[100vw] h-full p-5 min-h-[90vh] md:w-[80vw]">
        <div
          className="flex flex-col flex-1 overflow-y-auto h-[100%]"
          ref={chatResponseRef}
        >
          {messages.map((ele, index) => (
            <div
              key={index + ele[0]}
              className={`w-2/3 mb-2 p-3 rounded-lg text-xl break-words ${
                index % 2 === 0
                  ? "self-end bg-[var(--color-message-left-bg)]"
                  : "self-start bg-[var(--color-message-right-bg)]"
              } message`}
            >
              {index % 2 !== 0 && <AiIcon />}
              {index%2!=0?<ReactMarkdown>{ele[0]}</ReactMarkdown>:ele[0]}
              
              <br />
              <br />
              <h1 className="text-right text-[var(--color-secondary-text)]">
                {ele[1]} <ContentCopyIcon onClick={() => copyContent(ele[0])} />
              </h1>
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Response;
