from dataclasses import dataclass
from bs4 import Tag


@dataclass
class Quote:
    tags: list[str]
    author: str
    author_url: str
    quote: str

    def serialize(self) -> object:
        obj = self.__dict__.copy()
        del obj["author_url"]
        return obj


class QuoteParser:
    def __init__(self, tag: Tag) -> None:
        quote = tag.find(attrs={"class": "text"}).get_text()
        tags = [
            tag.get_text()
            for tag in tag.find(attrs={"class": "tags"}).find_all(
                attrs={"class": "tag"}
            )
        ]
        author_tag = tag.find(attrs={"class": "author"})
        author = author_tag.get_text()
        author_url = author_tag.find_next_sibling()["href"]
        self.data = Quote(tags=tags, author=author, author_url=author_url, quote=quote)
