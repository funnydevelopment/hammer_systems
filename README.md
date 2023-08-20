# Тестовое задание компании Hammer Systems

---
Реализация простой реферальной системы. Реализовать логику и API.
## Установка и запуск
1. Склонируйте репозиторий: 
`git clone git@github.com:funnydevelopment/hammer_systems.git`
2. Создайте и активируйте виртуальное окружение:
`python3 -m venv venv`
`source venv/bin/activate`
3. Установите зависимости:
`pip install -r requirements.txt`
4. Примените миграции:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
5. Запустите сервер:
`python3 manage.py runserver`

---
## Эндпоинты API

---
### Авторизация пользователя
**URL:** `/api/user_auth/`
**Метод:** POST
request
```json
{
  "phone_number": "+79995001122"
}
```
response
```json
{
  "result": true,
  "check_code": "1234"
}
```
---
### Получение кода авторизации
**URL:** `/api/user_auth/check_code/`
**Метод:** PATCH
request
```json
{
  "phone_number": "+79995001122",
  "check_code": "1234"
}
```
response_ok
```json
{
  "check_code_status": true,
  "auth_token": "xvfghjjgfdsthtgdrgdhdgsergdg"
}
```
response_error
```json
{
  "check_code_status": false
}
```
---
### Список приглашенных пользователей
**URL:** `/api/profile/`
**Метод:** GET
#### Headers:
#### Authorization: "xvfghjjgfdsthtgdrgdhdgsergdg"
response
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
response_error
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
response
```json
{
  "referral_link": null
}
```
response_error_token
```json
{
  "auth_token_status": false
}
```
response_error_referral_link_exist
```json
{
  "referral_link_exist": false
}
```
response_error_usage_once
```json
{
  "referral_link_was_used": true
}
```