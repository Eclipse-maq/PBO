import logging
from models import Product # wajib di impor dri models.py

LOGGER = logging.getLogger('REPOSITORY')

class ProductRepository:
    """mengambil data produk (simulasi database)"""
    def __init__(self):
        # data harcoded untuk simulasi
        self._products = {
            "P001": Product(id="P001", name="Laprop gaming", price=15000000),
            "P002": Product(id="P002", name="mouse wireless", price=2500000),
            "P003": Product(id="P003", name="keyboard mech", price=800000)
        }
        LOGGER.info("ProductRepository initialized with 3 products")

    def get_all(self) -> list[Product]:
        """mengambil semua produk yang tersedia"""
        return list(self._products.values())
    
    def get_by_id(self, product_id: str) -> Product | None:
        """mecari produk berdasarkan ID"""
        return self._products.get(product_id)