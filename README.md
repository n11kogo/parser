# Парсер новостей РИА

Этот проект предназначен для парсинга новостей с сайта РИА и сохранения их в формате JSON.

## Описание

Скрипт подключается к сайту РИА по заданному URL (в формате "https://ria.ru/.../"), собирает новости и сохраняет их в файл `news.json` в удобном формате.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_вашего_репозитория>
   cd parser
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Запустите основной скрипт:
```bash
python main.py
```

После выполнения появится файл `news.json` с результатами парсинга.

## Структура проекта

- `main.py` — основной скрипт запуска парсера.
- `parser.py` — модуль с логикой парсинга.
- `news.json` — файл, в который сохраняются новости.
- `requirements.txt` — список зависимостей.

## Требования

- Python 3.7+
- Интернет-соединение

## Контакты

Если у вас есть вопросы или предложения, создайте issue или свяжитесь с автором проекта. 

---

# RIA News Parser

This project is designed to parse news from the RIA website and save them in JSON format.

## Description

The script connects to the RIA website via a specified URL (in the format "https://ria.ru/.../"), collects news articles, and saves them to the `news.json` file in a convenient format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/n11kogo/parser
   cd parser
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python main.py
```

After execution, a `news.json` file with the parsed news will appear.

## Project Structure

- `main.py` — main script to run the parser.
- `parser.py` — module with parsing logic.
- `news.json` — file where news is saved.
- `requirements.txt` — list of dependencies.

## Requirements

- Python 3.7+
- Internet connection

## Contacts

If you have any questions or suggestions, create an issue or contact the project author. 
