from decorators import Module
from src.product.product_controller import ProductsController
from src.product.product_service import ProductService


@Module(
    controllers=[ProductsController], providers=[ProductService], imports=[],
)
class ProductModule:
    pass
