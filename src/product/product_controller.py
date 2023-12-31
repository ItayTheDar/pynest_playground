from fastapi import Depends
from .product_service import ProductService
from controller import Controller, Get


@Controller("products")
class ProductsController:

    product_service: ProductService = Depends(ProductService)

    @Get("/")
    def get_products(self):
        return self.product_service.get_product()
