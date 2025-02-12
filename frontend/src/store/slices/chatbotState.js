import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  messages:[],
  flag:true 
}

export const chatBotSlice = createSlice({
  name: 'chatBot',
  initialState,
  reducers: {
    userQuery: (state,action) => {
      state.messages.push(action.payload.message)
    },
    aiResponse: (state,action) => {
        if(action.payload.message != "Thinking......")state.messages.pop()
        state.messages.push(action.payload.message)
    },
    setflag:(state,action)=>{
      state.flag=action.payload.flag
    }
  },
})

export const { userQuery, aiResponse,setflag } = chatBotSlice.actions

export default chatBotSlice.reducer