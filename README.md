# Телеграм-бот: Транслитерация ФИО на латиницу

Этот репозиторий содержит телеграм-бота, который выполняет транслитерацию ФИО с кириллицы на латиницу в соответствии с **Приказом МИД России № 2113 от 12.02.2020**.

## Возможности

- Принимает ФИО на кириллице через сообщения в Телеграм.
- Возвращает транслитерацию ФИО на латиницу по официальным правилам.
- Логирует все взаимодействия и ошибки в файл. (Все логи сохраняются в файл mylog.log внутри контейнера.)
- Полностью контейнеризован с использованием Docker для упрощения развертывания.

---

## Структура файлов

- **`bot.py`** — основной код бота, написанный с использованием `aiogram`.
- **`Dockerfile`** — файл для сборки Docker-контейнера, включает переменную для токена бота.
- **`mylog.log`** — файл логов, где записываются все взаимодействия и ошибки.
- **`requirements.txt`** — список всех необходимых Python-зависимостей.

---

## Предварительные требования

- Установленный Docker.
- Токен Телеграм-бота. Создайте бота через [BotFather](https://core.telegram.org/bots#botfather) и скопируйте выданный токен.

---

## Для корректной работы необходимо собрать Docker-образ через аргумент сборки.

```bash
docker build --build-arg TOKEN=<ВАШ_ТОКЕН> -t telegram-translit-bot .
```


