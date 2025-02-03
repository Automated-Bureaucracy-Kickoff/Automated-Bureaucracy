import { useDispatch, useSelector } from "react-redux";
import CreateNewChat from "./CreateNewChat";
import { accessHistory } from "../redux/slices/chatbotState";
import { removeHistory } from "../redux/slices/previousChat";

function HistorySection() {
    const history = useSelector((state) => state.history.history);
    const dispatch = useDispatch();
  
    return (
      <div className="flex flex-col h-[80%] w-[80%] gap-2 ml-4">
        {/* Header: fixed height (flex-none) */}
        <div className="flex-none">
          <CreateNewChat />
        </div>
        {/* Scrollable area: fills remaining space */}
        <div className="flex-1 min-h-0 p-5 overflow-y-auto bg-[var(--color-secondary-bg)] dark:bg-[var(--color-secondary-bg)] rounded-xl shadow-lg gap-2">
          {history.map(({ title, messages }, idx) => (
            <div
              key={title + idx}
              onClick={() => {
                dispatch(accessHistory(history[idx]));
                dispatch(removeHistory(history[idx]));
              }}
              className="bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)] hover:bg-[var(--color-tertiary-bg)] dark:hover:bg-[var(--color-tertiary-bg)] transition-all duration-300 rounded-lg shadow-md cursor-pointer mb-4"
            >
              <h1 className="text-lg font-semibold text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)]">
                {title}
              </h1>
              <p className="text-sm text-[var(--color-secondary-text)] dark:text-[var(--color-secondary-text)]">
                {messages?.length || 0} messages
              </p>
            </div>
          ))}
        </div>
      </div>
    );
  }
  
  export default HistorySection;
  
