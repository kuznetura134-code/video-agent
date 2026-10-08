from fastapi import FastAPI
from pydantic import BaseModel
import time

# Создаем приложение (сервер)
app = FastAPI(title="Видео Агент Сервер")

# Описываем, какие данные мы ждем от клиента
class VideoRequest(BaseModel):
    prompt: str  # Русский текст
    scenes: int = 5  # Количество сцен (по умолчанию 5)

# Главная страница (чтобы проверить, что сервер жив)
@app.get("/")
def read_root():
    return {"status": "Сервер работает", "message": "Видео агент готов к работе"}

# Эндпоинт для генерации видео
@app.post("/generate_video")
def generate_video(request: VideoRequest):
    # Пока это ЗАГЛУШКА. Здесь будет реальная логика:
    # 1. Перевод RU -> EN
    # 2. Разбивка на сцены
    # 3. Вызов API видео-модели (MiniMax H3, Wan и т.д.)
    
    # Имитируем работу (задержка 2 секунды)
    time.sleep(2)
    
    # Возвращаем ответ клиенту
    return {
        "status": "success",
        "message": f"Задача принята! Промпт: '{request.prompt}'. Сцен: {request.scenes}.",
        "video_url": "https://example.com/video.mp4",  # Здесь будет реальная ссылка на видео
        "note": "Это заглушка. Реальное видео пока не генерируется."
    }
