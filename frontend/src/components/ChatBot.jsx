import Response from "./ChatResponse";
import Input from "./ChatInput";

const ChatBot = () => {
  return (
    <div
      className="flex flex-col h-full  w-full text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] rounded-[12px]  justify-between"
    >
        <div className= "flex overflow-auto">
            <Response />
        </div>
        <div>
            <Input />
        </div>
    </div>
  );
};

export default ChatBot;
