import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  history: JSON.parse(localStorage.getItem('chatHistory')) || []
}

const historySlice = createSlice({
  name: 'history',
  initialState,
  reducers: {
    appendHistory: (state, action) => {
      // Allow empty chats to be saved as configurations
      const newHistory = [action.payload, ...state.history];
      state.history = newHistory;
      localStorage.setItem('chatHistory', JSON.stringify(newHistory));
    },
    removeHistory: (state, action) => {
      const newHistory = state.history.filter(
        (chat) => chat.title !== action.payload.title
      );
      state.history = newHistory;
      localStorage.setItem('chatHistory', JSON.stringify(newHistory));
    },
    clearAllHistory: (state) => {
      state.history = [];
      localStorage.removeItem('chatHistory');
    }
  },
})

export const { appendHistory, removeHistory, clearAllHistory } = historySlice.actions
export default historySlice.reducer