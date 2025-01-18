# Changes to Commit When Your Model is Ready

## Query Submission and Execution Flow

When a user writes a query in the input tag and submits it, the following function will be executed:

### File: `src/controller/api-AI.js`

```javascript
// This AI function takes a string parameter (data) and returns a JSON object which has a schema {message: String } 
async function AI(data) {
  // 'data' will be the string containing the user's query from the input tag
}
```

---

## Tech Stack Used

### **Frontend**:  
- **Framework**: React  
  React was chosen for its component-based architecture and efficient rendering of UI.

### **State Management**:  
- **Redux Toolkit**:  
  Although the state management for this project is not highly complex, Redux Toolkit was used to simplify data handling and improve maintainability. It significantly enhances the developer experience by reducing boilerplate code.

### **AI**:  
- **Gemini**:  
  Gemini was selected as the AI engine for this project due to its free availability and reliable performance for natural language processing tasks.
