Вот документация для данного кода в указанном формате:

### 1. Функция NewAccessToken
```go
func NewAccessToken(userUUID string, ttl time.Duration) (string, error)
```
- Генерирует новый JWT-токен доступа с заданным UUID пользователя и временем жизни (ttl). Возвращает строку токена и ошибку (если есть).

### 2. Функция ParseAccessToken
```go
func ParseAccessToken(token string) (AccessTokenPayload, error)
```
- Парсит JWT-токен доступа и извлекает из него полезную нагрузку, включая UUID пользователя. Возвращает `AccessTokenPayload` и ошибку (если токен недействителен или произошла ошибка парсинга).