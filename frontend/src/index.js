import React from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import { BrowserRouter as Router } from 'react-router-dom'
import store from './store'
import App from './App'
import './styles/app.scss'

import { UserProvider } from './context/UserContext'

console.log("✅ index.js is running")

const root = createRoot(document.getElementById('root'))
root.render(
  <Provider store={store}>
    <UserProvider>
      <Router>
        <App />
      </Router>
    </UserProvider>
  </Provider>
)
