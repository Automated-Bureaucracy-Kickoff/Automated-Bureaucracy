import { useSelector } from "react-redux"
import ChatBot from "../components/ChatBot"
import HistorySection from "../components/HistorySection"
import Settings from "../components/Settings"


const MainPage = ()=>{
    const settingToggle = useSelector((state)=>state.toggle.settingsDisplay)
    return(
        <>
         <div style={{width:"80vw",position:"relative",height:"95vh",left:"20%",}} className="bg-black " >
         {settingToggle?<Settings/>:<ChatBot/>}
         </div>  
        <HistorySection/>
        </>
    )
}

export default MainPage