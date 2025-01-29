import { configureStore } from '@reduxjs/toolkit'
import chatBotReducres from "../slices/chatbotState"
import toggleReducres from "../slices/settings"
import historyReducres from "../slices/previousChat"

export const store = configureStore({
  reducer: {
    chatbot:chatBotReducres,
    toggle:toggleReducres,
    history:historyReducres

  },
  middleware: getDefaultMiddleware =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})