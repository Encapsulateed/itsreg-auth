Вот документация для указанного кода в нужном формате:

### Функция WaitForPort
```go
func WaitForPort(address string) bool
```
- Ожидает, пока указанный порт станет доступным для подключения.
- **Параметры:**
  - `address` — адрес в формате `"host:port"` для проверки доступности порта.
- **Возвращает:**
  - `bool` — `true`, если порт стал доступным в течение 5 секунд, иначе `false`. 

- **Описание работы:**
  - Функция запускает горутину, которая пытается установить TCP-соединение с указанным адресом с таймаутом в 1 секунду.
  - Если соединение успешно, горутина отправляет сигнал в канал `waitChan`.
  - Основная функция ждет либо сигнал из `waitChan`, либо истечения времени (5 секунд).