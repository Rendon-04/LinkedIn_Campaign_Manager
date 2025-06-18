import { configureStore } from '@reduxjs/toolkit'
import messageReducer from './features/messageSlice'

const store = configureStore({
  reducer: {
    message: messageReducer
  }
})

export default store
