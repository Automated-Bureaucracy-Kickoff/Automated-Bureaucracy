import './App.css'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { store } from './redux/store/store.js'
import ChatBot from './components/ChatBot.jsx'
import Navbar from './components/Navbar.jsx'
import MainPage from './pages/MainPage.jsx'
import HomePage from './pages/HomePage.jsx'

function App() {

  return (
    <BrowserRouter>
        <Provider store={store}>
            <div className="overflowremover flex flex-col w-screen h-screen  max-h-full  bg-zinc-100 dark:bg-zinc-900 dark:text-zinc-100">
                <Navbar/>
                <div className="flex w-full h-full">
                    <Routes>
                        {/* <Route path='/' element={<> <HomePage/> </>}/> */}
                        <Route path='/' element={<> <MainPage/>  </>} />
                        <Route path='/testing' element={<> <ChatBot /> </>} />
                    </Routes>
                </div>
            </div>
        </Provider>
    </BrowserRouter>
  )
}

export default App