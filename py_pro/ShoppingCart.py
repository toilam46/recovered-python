from typing import List

class ShoppingCart:
    def __init__(self):
        self.items: List[str] = []

    def add_item(self, item: str):
        self.items.append(item)

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)

    def get_items(self) -> List[str]:
        return self.items   
    