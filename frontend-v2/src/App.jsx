import './App.css'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { store } from './redux/store/store.js'
import ChatBot from './modules/Chatbot/pages/ChatBot.jsx'
import LandingPage from './modules/mainPage/pages/LandingPage.jsx'

function App() {

  return (
    <BrowserRouter>
    <Provider store={store}>

      <Routes>
        <Route path='/landingPage' element={<> <LandingPage/> </>} />
        <Route path='/mainPage' element={<> Lakshay </>} />
        <Route path='/testing' element={<> <ChatBot /> </>} />
      </Routes>


    </Provider>

  </BrowserRouter>
  )
}

export default App