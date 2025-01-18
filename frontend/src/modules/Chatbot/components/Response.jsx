import { useSelector } from "react-redux";

const Response = () => {
  const messages = useSelector((state) => state.chatbot.messages);

  return (
    <div className="response-container">
      {messages.map((ele, index) => (
        <div
          className={`message ${index % 2 !== 0 ? "message-right" : "message-left"}`}
          key={index}
        >
          {ele}
        </div>
      ))}
    </div>
  );
};

export default Response;
