import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"


const MainPage = ()=>{
    const settingToggle = useSelector((state)=>state.toggle.settingsDisplay)
    return(
        <>
         <div className="bg-tertiary-bg-light dark:bg-tertiary-bg-dark" >
            {settingToggle?<Settings/>:<ChatBot/>}
         </div>  
        <HistorySection/>
        </>
    )
}

export default MainPage