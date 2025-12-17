from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: str
    name: str
    price: float

@dataclass
class CartItems:
    product: Product
    quantity: int

    @property
    def subtotal(self) -> float:
        """menghitung subtotal unuk item ini"""
        return self.product.price * self.quantity