import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    settingsDisplay:false,
    setting:{
      "numAgents": 1,
      "prompts":["you are intelligent and be concise in 100 words","you are creative  and be concise in 100 words","you are practical and and be concise in 100 words"],
      "duration": "2",
      "model": "Model 1",
      "temperature": 1,
      "tools": {
          "webSearch": true,
          "notepad": true
      }
  }
}


export const settingSlice = createSlice({
  name: 'setting',
  initialState,
  reducers: {
   toggleSetting:(state,action)=>{
    state.settingsDisplay=!state.settingsDisplay
   },
   setSetting:(state,action)=>{
    state.setting=action.payload
   }
  },
})

export const { toggleSetting , setSetting} = settingSlice.actions

export default settingSlice.reducer