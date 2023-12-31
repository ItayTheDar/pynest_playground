from controller import Controller, Get, Post
from .management_service import ManagementService
from .management_model import Management

from fastapi import Depends


@Controller("management")
class ManagementController:
    management_service: ManagementService = Depends(ManagementService)

    @Get("/")
    def management(self):
        return self.management_service.get_managements()

    @Post("/")
    def add_management(self, management: Management):
        return self.management_service.add_management(management)
