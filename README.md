# Тестовое задание компании Hammer Systems

---
### POST /api/user_auth/
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
### PATCH /api/user_auth/check_code/
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
### GET /api/profile/
Headers:
Authorization: "xvfghjjgfdsthtgdrgdhdgsergdg"
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
### POST /api/profile/
Headers:
Authorization: "xvfghjjgfdsthtgdrgdhdgsergdg"
```json
{
  "invite_key": "key123"
}
```
response
```json
{
  "auth_token_status": true
}
```
response_error_token
```json
{
  "auth_token_status": false
}
```
response_error_invite_key_exist
```json
{
  "invite_key_exist": true
}
```
response_error_usage_once
```json
{
  "invite_key_was_used": true
}
```