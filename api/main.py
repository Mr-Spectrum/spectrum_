from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Создаем приложение
app = FastAPI()

# Разрешаем CORS-запросы
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Корневой маршрут (поскольку файл лежит в /api, этот путь на Vercel будет доступен по адресу /api)
@app.get("/api")
def read_root():
    return {"status": "Сервер работает отлично!"}

# Маршрут для вашей кнопки с именем
@app.get("/api/hello")
def say_hello_personally(name: str = "Гость"):
    # В FastAPI НЕ НУЖЕН jsonify! Достаточно просто вернуть обычный словарь (dict)
    return {"message": f"Привет, {name}!"}

