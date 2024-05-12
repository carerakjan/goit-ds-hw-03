from dataclasses import dataclass
from bs4 import Tag


@dataclass
class Author:
    fullname: str
    born_date: str
    born_location: str
    description: str

    def serialize(self) -> object:
        return self.__dict__.copy()


class AuthorParser:
    def __init__(self, tag: Tag) -> None:
        fullname = tag.find(attrs={"class": "author-title"}).get_text()
        born_date = tag.find(attrs={"class": "author-born-date"}).get_text()
        born_loc = tag.find(attrs={"class": "author-born-location"}).get_text()
        descr = tag.find(attrs={"class": "author-description"}).get_text()
        self.data = Author(
            fullname=fullname,
            born_date=born_date,
            born_location=born_loc,
            description=descr,
        )
