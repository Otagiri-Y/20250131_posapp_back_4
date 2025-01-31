from fastapi import FastAPI

# アプリケーションのインスタンスを作成
app = FastAPI()

# ルートエンドポイントの作成
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}