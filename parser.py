from dataclasses import dataclass, asdict
import requests
from bs4 import BeautifulSoup
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

@dataclass
class NewsItem:
    url: str | None
    date: str | None
    title: str | None
    text: str | None

class RiaNews:
    def __init__(self, url, headers=headers):
        self.url = url
        self.headers = headers

    def get_article_links(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        links = set()
        for a in soup.find_all("a", class_="list-item__title", href=True):
            href = a["href"]
            if href.startswith("/"):
                href = "https://ria.ru" + href
            links.add(href)
        return list(links)

    def get_article_date(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        date_tag = soup.find("div", class_="article__info-date")
        if date_tag and date_tag.get_text(strip=True):
            return date_tag.get_text(strip=True)
        time_tag = soup.find("time")
        if time_tag:
            if time_tag.has_attr("datetime"):
                return time_tag["datetime"]
            if time_tag.get_text(strip=True):
                return time_tag.get_text(strip=True)
        span_tag = soup.find("span", class_="date")
        if span_tag and span_tag.get_text(strip=True):
            return span_tag.get_text(strip=True)
        return None

    def get_article_title(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        article_title = soup.find("div", class_="article__title")
        if article_title and article_title.get_text(strip=True):
            return article_title.get_text(strip=True)
        title = soup.find("title")
        if title and title.get_text(strip=True):
            return title.get_text(strip=True)
        return None

    def get_article_text(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        article_text = soup.find("div", class_="article__text")
        if article_text and article_text.get_text():
            return article_text.get_text()
        article_block = soup.find("div", class_="article__block")
        if article_block and article_block.get_text():
            return article_block.get_text()
        return None

    def get_news(self):
        news = []
        links = self.get_article_links()
        for link in links:
            date = self.get_article_date(link)
            title = self.get_article_title(link)
            text = self.get_article_text(link)
            news.append(NewsItem(url=link, date=date, title=title, text=text))
        return news

