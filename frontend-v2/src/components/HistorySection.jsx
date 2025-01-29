import { useDispatch, useSelector } from "react-redux";
import CreateNewChat from "./CreateNewChat";
import { accessHistory } from "../redux/slices/chatbotState";

function HistorySection() {
  const history = useSelector((state) => state.history.history);
  const dispatch = useDispatch();

  return (
    <>
      <CreateNewChat />
      <div
        className="fixed top-20 left-3 mt-9 w-[18vw] min-h-[75vh]  rounded-xl p-4 shadow-lg"
      >
        {history.map(({ title, messages, timestamp }, idx) => (
          <div
            key={title + idx}
            onClick={() => dispatch(accessHistory(history[idx]))}
            className="bg-black hover:bg-gray-800 transition-all duration-300 rounded-lg p-4 cursor-pointer mb-3 shadow-md"
          >
            <h1 className="text-white text-lg font-semibold">{title}</h1>
            <p className="text-gray-400 text-sm">{messages?.length || 0} messages</p>

          </div>
        ))}
      </div>
    </>
  );
}

export default HistorySection;
