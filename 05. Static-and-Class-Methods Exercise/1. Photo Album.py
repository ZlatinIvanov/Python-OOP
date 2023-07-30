import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.current_row_index = 0

    def __initialize_photos(self) -> List[List[str]]:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        self.photos[self.current_row_index].append(label)

    def display(self):
        pass

p = PhotoAlbum(2)
a = 5