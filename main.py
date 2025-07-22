import json
from parser import RiaNews
from dataclasses import asdict 

URL_Ria = "https://ria.ru/.../"

def main():
    ria = RiaNews(URL_Ria)
    news = ria.get_news()
    # Сохраняем в JSON
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump([asdict(item) for item in news], f, ensure_ascii=False, indent=2)
    print(f"Сохранено новостей: {len(news)}")


if __name__ == "__main__":
    main()
