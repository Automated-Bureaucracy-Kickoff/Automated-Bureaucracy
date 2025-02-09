import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"
import { useEffect } from "react"
import { useLocation } from "react-router-dom"


const MainPage = () => {
    const settingToggle = useSelector((state) => state.toggle.settingsDisplay)
    let location = useLocation()   
    useEffect(()=>{
        // when this MainPage component shifts need to change below pathname 
        if(location.pathname=="/main")document.querySelector(".overflowremover").style.overflowY="hidden"
    },[])
    return (  
        <>
            <div className="flex w-full h-full bg-[var(--color-primary-bg)] dark:bg-[var(--color-primary-bg)]">
                <div className = "hidden xs:hidden  md:flex h-full w-1/3">
                    <HistorySection />
                </div>
                <div className = "flex w-full h-full">
                    {settingToggle ? <Settings /> : <ChatBot />}
                </div>
            </div>
        </>
    )
}

export default MainPage