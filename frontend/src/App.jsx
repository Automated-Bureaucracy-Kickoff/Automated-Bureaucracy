import './App.css'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Routes, useLocation } from 'react-router-dom'
import { store } from './redux/store/store.js'
import Navbar from './components/Navbar.jsx'
import MainPage from './pages/MainPage.jsx'
import LandingPage from './pages/HomePage.jsx'
import LandingNavbar from './components/landingPageNavbar.jsx'
import { useEffect } from 'react'
import AboutUsPage from './pages/AboutUsPage'
import useScrollToTop from './hooks/useScrollToTop'

function ScrollToTop() {
  useScrollToTop();
  return null;
}

function App() {
    return (
        <BrowserRouter>
            <Provider store={store}>
                <ScrollToTop />
                <Routes>
                    {/* <Route path='/' element={<> <HomePage/> </>}/> */}
                    <Route path='/' element={<>
                        <LandingNavbar />
                        <LandingPage />
                    </>} />
                    <Route path='/main' element={
                        <div className="overflowremover flex flex-col w-screen h-screen  max-h-full  bg-zinc-100 dark:bg-zinc-900 dark:text-zinc-100">
                            <Navbar />
                            <div className="flex w-full h-full">
                                <MainPage />
                            </div>
                        </div>
                    } />
                    <Route path='/aboutus' element={<>
                        <LandingNavbar />
                        <AboutUsPage />
                    </>} />
                </Routes>
            </Provider>
        </BrowserRouter>
    )
}

export default App