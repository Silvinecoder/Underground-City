import json

from config_helper.db.query_helper import add_default_equality_operator
from config_helper.endpoints.decorators import protected
from config_helper.enpoint import Endpoint
from config_helper.log import log_config

log = log_config("ProductEndpoint")

class Product(Endpoint):
    def __init__(self):
        super().__init__("product", "products")

    @protected("accounts")
    def get_global(self, event, accounts[]):
        default_filter = {
            add_default_equality_operator("accounts", accounts)
        }
        return self.get_global_with_filter(event, default_filter)