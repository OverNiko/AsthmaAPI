# Asthma API

Asthma API — это RESTful API для управления пользователями и симптомами.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/OverNiko/AsthmaAPI.git
   cd your_repository

2. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt

4. Создайте файл .env в корне проекта и добавьте переменные окружения:

   ```bash
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/asthma_db

## Запуск

1. Запустите сервер разработки:

   ```bash
   uvicorn main:app --reload

2. API будет доступен по адресу: http://127.0.0.1:8000/docs

## Tестирование

Для тестирования API используйте Postman или другой HTTP-клиент. Примеры эндпоинтов:

- Регистрация пользователя: POST /auth/register
- Авторизация: POST /auth/login
- Получение профиля: GET /auth/profile
- Добавление симптомов: POST /symptoms
- История симптомов: GET /symptoms/history

## Зависимости

- Python 3.10+
- FastAPI
- SQLAlchemy
- asyncpg
- Uvicorn
- python-jose
- passlib
- python-dotenv
