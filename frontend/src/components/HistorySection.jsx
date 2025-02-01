import { useDispatch, useSelector } from "react-redux";
import CreateNewChat from "./CreateNewChat";
import { accessHistory } from "../redux/slices/chatbotState";
import { removeHistory } from "../redux/slices/previousChat";

function HistorySection() {
  const history = useSelector((state) => state.history.history);
  const dispatch = useDispatch();
 
      
  return (
    <>
      <CreateNewChat />
      <div
        className="relative h-full w-full m-6 w-1/8 h-3/4 rounded-xl p-5 shadow-lg bg-[var(--color-secondary-bg)] dark:bg-[var(--color-secondary-bg)]; overflow-y-auto z-10">
        {history.map(({ title, messages, timestamp }, idx) => (
          <div
            key={title + idx}
            onClick={() => {dispatch(accessHistory(history[idx])); dispatch(removeHistory(history[idx]));}}
            className="bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)] 
                   hover:bg-[var(--color-tertiary-bg)] dark:hover:bg-[var(--color-tertiary-bg)] 
                   transition-all duration-300 rounded-lg p-4 cursor-pointer mb-3 shadow-md"
          >
            <h1 className="text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] text-lg font-semibold">
              {title}
            </h1>
            <p className="text-[var(--color-secondary-text)] dark:text-[var(--color-secondary-text)] text-sm">
              {messages?.length || 0} messages
            </p>
          </div>
        ))}
      </div>
    </>

  );
}

export default HistorySection;
