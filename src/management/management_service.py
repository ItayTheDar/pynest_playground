from decorators import Injectable
from functools import lru_cache
from .management_model import Management
from typing import List


@lru_cache()
@Injectable
class ManagementService:

    def __init__(self):
        self.database: List[Management] = []

    def get_managements(self):
        return self.database

    def add_management(self, management: Management):
        self.database.append(management)
        return management
