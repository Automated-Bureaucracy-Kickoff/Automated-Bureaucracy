import { createSlice } from '@reduxjs/toolkit'
import { appendHistory } from './previousChat'

const initialState = {
  messages:[],
  files:[],
  title:"Default Title",
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
      state.messages=[]
      state.files=[]
      state.title=""
      
    },
    createTitle:(state,action)=>{
      state.title=action.payload
    },
    accessHistory:(state,action)=>{
      console.log(action.payload)
      
      const {messages,files,title}=action.payload
      state.messages=messages
      state.files=files
      state.title=title
    }
  },
})

export const { userQuery, aiResponse,setflag,appendFiles,createHistory,createTitle,accessHistory } = chatBotSlice.actions

export default chatBotSlice.reducer