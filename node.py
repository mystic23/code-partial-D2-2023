from typing import List

class Nodo:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return  f" {self.value}"
