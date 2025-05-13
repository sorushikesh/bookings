import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/v1/user", tags=["User"])

class UserHandler:
    def __init__(self, user: User):
        self.user = user