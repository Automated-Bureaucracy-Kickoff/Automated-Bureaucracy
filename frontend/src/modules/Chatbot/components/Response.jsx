import { useSelector } from "react-redux";

const Response = () => {
    const messages = useSelector((state) => state.chatbot.messages);
  
    return (
      <div className="m-4 flex flex-col w-full h-full overflow-auto">
        {messages.map((ele, index) => (
          <div
            className={`flex ${index % 2 === 0 ? "justify-start" : "justify-end"}`}
            key={index}
          >
            <div
              className={`max-w-[550px] p-3 m-4 rounded-lg text-base word-wrap break-words ${
                index % 2 === 0 ? "bg-blue-100 text-left" : "bg-gray-200 text-right"
              }`}
            >
              {ele}
            </div>
          </div>
        ))}
      </div>
    );
  };

export default Response;
