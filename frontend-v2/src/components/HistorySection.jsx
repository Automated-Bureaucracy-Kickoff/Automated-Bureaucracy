import CreateNewChat from "./CreateNewChat";

function HistorySection() {
  return (
    <>
      <CreateNewChat />
      <div className="border-2 bg-secondary-bg-light dark:bg-secondary-bg-dark border-primary-accent-light dark:border-primary-accent-dark fixed top-[150px] left-[20px] rounded-xl p-6 w-[75%]">
        {/* Add your history content here */}
      </div>
    </>
  );
}

export default HistorySection;
