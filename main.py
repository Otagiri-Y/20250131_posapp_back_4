from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# アプリケーションのインスタンスを作成
app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド
    allow_headers=["*"],  # 許可するHTTPヘッダー
)

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}
