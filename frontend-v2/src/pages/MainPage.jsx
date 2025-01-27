import { ClassNames } from "@emotion/react"
import ChatBot from "./ChatBot"
import { useEffect } from "react"


const MainPage = ()=>{

    return(
        <>
         <div style={{width:"80vw",position:"relative",height:"95vh",left:"20%",overflow:"hidden"}} className="bg-black " >
         <ChatBot/>
         </div> 
        
        
        </>
    )
}

export default MainPage