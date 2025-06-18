import { createSlice } from '@reduxjs/toolkit'

export const messageSlice = createSlice({
  name: 'message',
  initialState: {
    content: '',
    loading: false
  },
  reducers: {
    setMessage: (state, action) => {
      state.content = action.payload
    },
    setLoading: (state, action) => {
      state.loading = action.payload
    }
  }
})

export const { setMessage, setLoading } = messageSlice.actions
export default messageSlice.reducer
