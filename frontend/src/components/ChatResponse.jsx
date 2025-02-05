import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import AiIcon from "./AIicon";
import EditIcon from "@mui/icons-material/Edit";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import { copyContent } from "../controller/api-copy";
import ChangeTitle from "./ChangeTitle";

const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);
  const title = useSelector((state) => state.chatbot.title);
  const [changetitle, setChangetitle] = useState(false);
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
      <div className="fixed z-20 m-4 text-[var(--color-primary-text)] text-3xl font-bold p-4 text-left w-full">
        {title || "Default Title"}
        <EditIcon
          className="relative -left-1 top-1 cursor-pointer"
          style={{ height: "20px", color: "var(--color-secondary-text)" }}
          onClick={() => setChangetitle(true)}
        />
      </div>
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
              {ele[0]}
              <br />
              <br />
              <h1 className="text-right text-[var(--color-secondary-text)]">
                {ele[1]} <ContentCopyIcon onClick={() => copyContent(ele[0])} />
              </h1>
            </div>
          ))}
        </div>
        {changetitle && <ChangeTitle setChangetitle={setChangetitle} />}
      </div>
    </>
  );
};

export default Response;
