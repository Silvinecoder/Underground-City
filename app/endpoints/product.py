import json

from config_helper.enpoint import Endpoint
from config_helper.log import log_config

log = log_config("ProductEndpoint")

class Product(Endpoint):
    def __init__(self):
        super().__init__("product", "products")

    