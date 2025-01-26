import './App.css'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { store } from './redux/store/store.js'
import ChatBot from './pages/ChatBot.jsx'
import LandingPage from './pages/HomePage.jsx'
import Navbar from './components/Navbar.jsx'

function App() {

  return (
    <BrowserRouter>
        <Provider store={store}>
            <div className="w-screen h-screen bg-zinc-100 dark:bg-zinc-900 dark:text-zinc-100">
                <Navbar></Navbar>
                <Routes>
                    <Route path='/' element={<> <LandingPage/> </>}/>
                    <Route path='/mainPage' element={<> Lakshay </>} />
                    <Route path='/testing' element={<> <ChatBot /> </>} />
                </Routes>
            </div>
        </Provider>
    </BrowserRouter>
  )
}

export default App