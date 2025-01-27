import { configureStore } from '@reduxjs/toolkit'
import chatBotReducres from "../slices/chatbotState"

export const store = configureStore({
  reducer: {
    chatbot:chatBotReducres
  },
  middleware: getDefaultMiddleware =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})