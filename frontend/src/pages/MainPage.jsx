import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"


const MainPage = () => {
    const settingToggle = useSelector((state) => state.toggle.settingsDisplay)
    return (
        <>
            <div className="flex w-full h-full bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)] overflow-auto">
                <div className = "h-full w-1/4">
                    <HistorySection />
                </div>
                <div>
                    {settingToggle ? <Settings /> : <ChatBot />}
                </div>
            </div>
        </>
    )
}

export default MainPage