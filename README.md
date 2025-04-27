# Asthma API

Asthma API — это RESTful API для управления пользователями и симптомами.

## Требования

- Python 3.10+
- PostgreSQL 12+

## Структура проекта

asthma_api/ 
├── models/ # SQLAlchemy модели 
├── routes/ # Маршруты FastAPI 
├── schemas/ # Pydantic-схемы 
├── utils.py # Утилиты (хеширование, токены и т.д.) 
├── config.py # Конфигурация проекта 
├── main.py # Точка входа в приложение 
└── README.md # Документация

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/OverNiko/AsthmaAPI.git
   cd AsthmaAPI

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

5. Таблици для базы данных достуаны в файле: init_db.sql

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

## Примеры запросов

### Регистрация пользователя

**POST /auth/register**

Тело запроса:
```json
{
  "name": "Test User",
  "email": "testuser@example.com",
  "password": "testpassword123"
}

### Авторизация

**POST /auth/login**

Тело запроса:
```json
{
  "email": "testuser@example.com",
  "password": "testpassword123"
}

Ответ:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

### Получение профиля

**GET /auth/profile**

Заголовок:
Authorization: Bearer <access_token>

Ответ:
```json
{
  "id": 1,
  "name": "Test User",
  "email": "testuser@example.com"
}

### Добавление симптомов

**POST /symptoms**

Заголовок:
Authorization: Bearer <access_token>

Тело запроса:
```json
{
  "cough_level": 7,
  "breathlessness": 5
}

Ответ:
```json
{
  "id": 1,
  "cough_level": 7,
  "breathlessness": 5,
  "timestamp": "2025-04-27T12:00:00Z"
}

### История симптомов

**GET /symptoms/history**

Заголовок:
Authorization: Bearer <access_token>

Ответ:
```json
{
  {
    "id": 1,
    "cough_level": 7,
    "breathlessness": 5,
    "timestamp": "2025-04-27T12:00:00Z"
  },
  {
    "id": 2,
    "cough_level": 3,
    "breathlessness": 2,
    "timestamp": "2025-04-26T15:30:00Z"
  }
}

## Зависимости

- Python 3.10+
- FastAPI
- SQLAlchemy
- asyncpg
- Uvicorn
- python-jose
- passlib
- python-dotenv
