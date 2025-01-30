import Response from "./ChatResponse";
import Input from "./ChatInput";

const ChatBot = () => {
  return (
    <div
      className="text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] p-0 m-2 min-w-full  overflow-hidden rounded-[12px]"
    >
      <Response />
      <Input />
    </div>
  );
};

export default ChatBot;
