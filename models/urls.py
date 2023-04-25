from dataclasses import dataclass

@dataclass(slots=True)
class URLs:

    long_url: str
    short_url: str
    _id: str = ""
    clicks: int = 0

    @property
    def to_json(self) -> dict:
        return {
            "longUrl": self.long_url,
            "shortUrl": self.short_url,
            "clicks": self.clicks
        }