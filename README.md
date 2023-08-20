# Тестовое задание компании Hammer Systems

Реализация простой реферальной системы. Реализовать логику и API.

---
## Шаги по настройке PostgreSQL для Django проекта
1. **Установите PostgreSQL**: Если PostgreSQL еще не установлен на вашем компьютере, выполните установку в соответствии с документацией для вашей операционной системы.
2. Обновите настройки Django: Откройте файл settings.py вашего Django проекта и обновите настройки базы данных:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## Установка и запуск
1. Склонируйте репозиторий: 
`git clone git@github.com:funnydevelopment/hammer_systems.git`
2. Создайте и активируйте виртуальное окружение:
`python3 -m venv venv`
`source venv/bin/activate`
3. Установите зависимости:
`pip install -r requirements.txt`
4. Примените миграции:
`python3 manage.py migrate`
5. Запустите сервер:
`python3 manage.py runserver`

---
## Эндпоинты API

### Авторизация пользователя
**URL:** `/api/user_auth/`  
**Метод:** POST  
Request - отправляем номер пользователя
```json
{
  "phone_number": "+79995001122"
}
```
Response - получаем код авторизации
```json
{
  "result": true,
  "check_code": "1234"
}
```

### Получение кода авторизации
**URL:** `/api/user_auth/check_code/`  
**Метод:** PATCH  
Request - отправляем код авторизации
```json
{
  "phone_number": "+79995001122",
  "check_code": "1234"
}
```
Response - получаем токен, если код правильный, который используем дальше
```json
{
  "check_code_status": true,
  "auth_token": "xvfghjjgfdsthtgdrgdhdgsergdg"
}
```
Response - ответ, если код не совпал
```json
{
  "check_code_status": false
}
```

### Список приглашенных пользователей
**URL:** `/api/profile/`  
**Метод:** GET
#### Headers:
#### Authorization: "xvfghjjgfdsthtgdrgdhdgsergdg"
Response - получаем список приглашенных пользователей
```json
{
  "auth_token_status": true,
  "phone_number": "+79995001122",
  "referral_link": "asd123",
  "invited_users": [ 
    {
      "phone_number": "+79996422233",
      "referral_link": "dwa852"
    },
    {
      "phone_number": "+79996410213",
      "referral_link": "ebr524"
    }
  ]
}
```
Response - ответ, если токен другой
```json
{
  "auth_token_status": false
}
```
### Использование реферальной ссылки
**URL:** `/api/profile/`  
**Метод:** POST
#### Headers:
#### Authorization: "xvfghjjgfdsthtgdrgdhdgsergdg"
```json
{
  "referral_link": "key123"
}
```
Response - реферальная ссылка еще существует
```json
{
  "referral_link": null
}
```
Response - невалидный токен
```json
{
  "auth_token_status": false
}
```
Response - ответ, если реферальная ссылка уже существует
```json
{
  "referral_link_exist": false
}
```
Response - ответ, если реферальная ссылка была использована ранее
```json
{
  "referral_link_was_used": true
}
```