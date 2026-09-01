from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Создаем приложение
app = FastAPI()

# Добавляем разрешение, чтобы сайт мог общаться с бэкендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Корневой маршрут (чтобы проверить, что сервер вообще живой)
@app.get("/")
def read_root():
    return {"status": "Сервер работает отлично!"}

# Маршрут для вашей кнопки
@app.get("/api/greet")
def say_hello():
    return {"message": "Привет! Этот текст прилетел прямиком из бэкенда на Python!"}

# Новый маршрут, который принимает имя (name) в качестве параметра
@app.get("/api/hello")
def say_hello_personally(name: str = "Гость"):
    return jsonify({"message": f"Привет, {name}!"})
