import { configureStore } from '@reduxjs/toolkit'
import chatBotReducres from "../slices/chatbotState"
import toggleReducres from "../slices/settings"

export const store = configureStore({
  reducer: {
    chatbot:chatBotReducres,
    toggle:toggleReducres

  },
  middleware: getDefaultMiddleware =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})