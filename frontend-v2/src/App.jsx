import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard'
import Home from './pages/Home'

import './App.css'
import TopNav from './components/TopNav';

function App() {
    return (
      <Router>
        <TopNav/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<Dashboard />} />
        </Routes>
      </Router>
    );
  }

export default App
