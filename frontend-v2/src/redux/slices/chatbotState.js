import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  messages:[],
  saved:[],
  files:[],
  flag:true 
}

//
export const chatBotSlice = createSlice({
  name: 'chatBot',
  initialState,
  reducers: {
    userQuery: (state,action) => {
      state.messages.push(action.payload.message)
      
    },
    aiResponse: (state,action) => {
        if(state.messages[state.messages.length-1][0]== "Thinking......"){
          state.messages[state.messages.length-1][0]=action.payload.message
          return
        }
        state.messages.push(action.payload.message)
    },
    appendFiles:(state,action)=>{
      console.log(action.payload)
      state.files.push(action.payload.files)
    },
    setflag:(state,action)=>{
      state.flag=action.payload.flag
    },
    createHistory:(state)=>{
      state.saved.push({
        message:state.messages,
        files:state.files
      })
      state.messages=[]
      state.files=[]
    },
    createTitle:(state,action)=>{

    }
  },
})

export const { userQuery, aiResponse,setflag,appendFiles,createHistory } = chatBotSlice.actions

export default chatBotSlice.reducer