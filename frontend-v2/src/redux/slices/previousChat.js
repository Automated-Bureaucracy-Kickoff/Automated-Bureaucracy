import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  history:[],
}

export const chatHistorySlice = createSlice({
  name: 'chatHistory',
  initialState,
  reducers: {
    appendHistory:(state,action)=>{
        state.history.push(action.payload)
    },
    removeHistory:(state,action)=>{
      // console.log("removeHistory",action.payload)
      // state.history.filter((ele)=>ele!=action.payload)
      
    }
    // getHistory: (state, action) => {
    //   state.history = state.history.filter(
    //     (ele) => ele.title === action.payload.title && ele.key === action.payload.key
    //   );
    // }
  },
})

export const { appendHistory,removeHistory } = chatHistorySlice.actions

export default chatHistorySlice.reducer