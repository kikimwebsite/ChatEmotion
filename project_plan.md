# **Project Plan: Real-Time Live Chat with Emotion Analysis**

## **Flow Breakdown**
1. **Frontend (Next.js + TypeScript + Apollo Client + WebSocket)**:
   - The user types a message in the live chat UI.
   - The text input is sent via GraphQL and WebSocket to the backend.

2. **Backend (Python + FastAPI + WebSocket + Graphene)**:
   - Receives the text input from the frontend using GraphQL.
   - Processes the text input using the Python emotion analysis of BERT from Hugging Face PyTorch model file.
   - Returns an array of detected emotions and their scores (e.g., `[{label: "joy", score: 0.65}, ...]`).
   - Sends the results back to the frontend using WebSocket + GraphQL.

3. **Frontend**:
   - Displays the original text alongside a chart or graph of the detected emotions in the live chatroom UI.