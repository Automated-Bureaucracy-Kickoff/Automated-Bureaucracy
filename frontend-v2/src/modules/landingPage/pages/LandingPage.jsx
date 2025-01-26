import { Button } from "@mui/material";
import Navbar from "../components/Navbar";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
function LandingPage() {


    return (
        <>
            MATERIAL UI IS WORKING
            <Button variant="text">Text</Button>
            <Button variant="contained">Contained</Button>
            <Button variant="outlined">Outlined</Button>

            <br />
            <div className="p-10 bg-blue-500 text-white text-center">
                <h1 className="text-4xl font-bold">Tailwind CSS is Working!</h1>
            </div>
            <br />
            MATERIAL UI ICON IS WORKING
            <ArrowBackIcon />

            MATERIAL UI WITH TAILWIND
            <div className="flex justify-center items-center h-screen">
                <Button
                    variant="contained"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                    MUI Button with Tailwind
                </Button>
            </div>

        </>
    )
}

export default LandingPage