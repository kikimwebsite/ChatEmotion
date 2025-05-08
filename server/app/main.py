from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp
from app.schema import schema
from app.emotion import run_and_display_nonzero_emotions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQLApp(schema=schema))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            
            emotion_results = run_and_display_nonzero_emotions(data)
            
            await websocket.send_json({
                "text": data,
                "emotions": [
                    {"label": label, "score": score} for label, score in emotion_results
                ]
            })
    except WebSocketDisconnect:
        print("WebSocket disconnected.")


