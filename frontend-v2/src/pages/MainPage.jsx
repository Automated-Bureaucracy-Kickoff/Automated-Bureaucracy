import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"


const MainPage = () => {
    const settingToggle = useSelector((state) => state.toggle.settingsDisplay)
    return (
        <>
            <div className="w-[80vw] relative h-[95vh] left-[20%] bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)]">
                {settingToggle ? <Settings /> : <ChatBot />}
            </div>
            <HistorySection />

        </>
    )
}

export default MainPage