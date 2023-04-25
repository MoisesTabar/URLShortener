from repositories import IRepository
from services import shorten_url
from models import Url, URLs

class URLShortenerUseCase:

    def __init__(self, repository: IRepository) -> None:
        self.repository = repository

    def verify_url_existence_use_case(self, url: Url) -> dict:
        document = self.repository.get_one({"longUrl": url.value})

        if document:
            return { "result": f"The URL: {url.value} is already registered" }
        
        return { "result": "OK" }
    

    def shorten_an_url_use_case(self, url: Url) -> str:
        shortened_url: str = shorten_url(url.value)

        model: URLs = URLs(
            long_url=url.value,
            short_url=shortened_url
        )

        document = self.repository.add(model)

        if not document.acknowledged:
            return f"The URL: {url.value} could not be reversed. Try again."
        
        return shortened_url


    def top_visited_urls_use_case(self) -> list[dict]:
        documents = self.repository.get()

        urls = [
            URLs(
                long_url=doc["longUrl"],
                short_url=doc["shortUrl"],
                clicks=doc["clicks"]
            ).to_json for doc in documents
        ]

        top_visited = sorted(urls, key=lambda x: x["clicks"], reverse=True)

        return top_visited


    def update_url_clicks_use_case(self, url: str) -> dict:
        query: dict = {"$or": [{"longUrl": url}, {"shortUrl": url}]}
        values: dict = {"$inc": {"clicks": 1}}

        update = self.repository.update(query, values)

        if not update:
            return { "result": "Failed to update click amount" }
        
        return { "result": "OK", "document": update }