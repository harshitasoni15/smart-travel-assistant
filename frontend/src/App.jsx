import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { TravelPlanner } from '@/components/TravelPlanner'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TravelPlanner />} />
      </Routes>
    </Router>
  )
}

export default App
