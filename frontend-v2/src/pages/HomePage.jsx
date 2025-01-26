
import Button from '@mui/material/Button';

function HomePage() {


    return (
        <>
            <div className="flex flex-col dark:text-white m-8 p-8 rounded">
                <div className = "flex justify-between bg-zinc-300 dark:bg-zinc-700 rounded p-4 m-4">
                    <div className="flex flex-col flex-grow justify-center space-y-4 items-center">
                        <h1 className="text-2xl">Agents to help with the things no one wants to do</h1>
                        <h2 className="text-xl ">Customizable agents to speed up and automate everyday tasks for the working professional. From coding to research and documentation. Automated Bureaucracy has your back</h2>
                        <div className = "flex space-x-4">
                            <Button variant="contained">Watch Example</Button>
                            <Button variant="contained">Start Exploring</Button>
                        </div>
                    </div>
                    <div className="flex justify-center items-center w-1/2 shrink-0 h-64 bg-black rounded">
                    </div>
                </div>
                <div className='flex flex-col justify-center p-16'>
                    <h1 className="text-3xl text-center p-4">Meet our agents</h1>
                    <div className="flex space-x-8">
                        <div className="flex-1 border-2 p-2 rounded">
                            <h2 className="text-xl text-center">Coding Agent</h2>
                            <h3>loren ipsum</h3>
                        </div>
                        <div className="flex-1 border-2 p-2 rounded">
                            <h2 className="text-xl text-center">Research Agent</h2>
                            <h3>loren ipsum</h3>
                        </div>
                        <div className="flex-1 border-2 p-2 rounded">
                            <h2 className="text-xl text-center">Documentation Agent</h2>
                            <h3>loren ipsum</h3>
                        </div>
                    </div>
                </div>
                <div>

                </div>
            </div>
        </>
    )
}

export default HomePage