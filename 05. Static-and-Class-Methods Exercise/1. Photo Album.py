from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[str] = []

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pass

    def add_photo(self, label: str):
        pass

    def display(self):
        passe

