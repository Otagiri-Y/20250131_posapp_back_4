import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

load_dotenv()

# アプリケーションのインスタンスを作成
app = FastAPI()

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド
    allow_headers=["*"],  # 許可するHTTPヘッダー
)

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Azure で PORT 環境変数が設定される場合に対応
    uvicorn.run(app, host="0.0.0.0", port=port)