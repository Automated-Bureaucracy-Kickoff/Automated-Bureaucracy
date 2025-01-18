import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  messages:[],
}

export const chatBotSlice = createSlice({
  name: 'chatBot',
  initialState,
  reducers: {
    userQuery: (state,action) => {
      state.messages.push(action.payload.message)
    },
    aiResponse: (state,action) => {
        state.messages.push(action.payload.message)
    }
  },
})

export const { userQuery, aiResponse } = chatBotSlice.actions

export default chatBotSlice.reducer