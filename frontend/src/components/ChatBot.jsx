import Response from "./ChatResponse";
import Input from "./ChatInput";

const ChatBot = () => {
  return (
    <div
      className="h-full w-full text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] overflow-hidden rounded-[12px]"
    >
        <div className= "flex flex-grow overflow-auto">
            <Response />
        </div>
        <div>
            <Input />
        </div>
    </div>
  );
};

export default ChatBot;
