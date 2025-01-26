import Response from "../components/Response";
import Input from "../components/Input";

const ChatBot = () => {
  return (
    <div className="h-full flex flex-col flex-grow font-medium justify-between  items-center">
      <Response />
      <Input/>
    </div>
  );
};

export default ChatBot;
