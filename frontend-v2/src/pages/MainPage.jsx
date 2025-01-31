import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"


const MainPage = () => {
    const settingToggle = useSelector((state) => state.toggle.settingsDisplay)
    return (
        <>
            <div className="absolute w-[80vw] top-[10vh] left-[40vh]  bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)] overflow-auto max-h-[88vh]">
                {settingToggle ? <Settings /> : <ChatBot />}
            </div>
            <HistorySection />

        </>
    )
}

export default MainPage