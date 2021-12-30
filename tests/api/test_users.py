import os

import pytest
from httpx import AsyncClient

from app.main import create_application
from app.services.functions import Expensive

USER_NOT_FOUND_MSG = "User not found"
USERS_PREFIX = "api/users"
USERS_SERVICE_URL = "http://app-db-test/"

user = {
    "name": "test",
    "username": "test",
    "password": os.getenv("USER_PASSWORD"),
}

user_update = {
    "name": "test1",
    "username": "test1",
    "password": os.getenv("USER_PASSWORD_UPDATE"),
}

user_update2 = {
    "name": "test1",
    "username": "test1",
    "password": os.getenv("USER_PASSWORD_UPDATE"),
}

user2 = {
    "name": "test2",
    "username": "test2",
    "password": os.getenv("USER_2_PASSWORD"),
}

app = create_application()

@pytest.mark.asyncio
async def test_create(monkeypatch):
    async def mock_get(self):
        return "hello_world"
        
    #monkeypatch.setattr(Expensive,"expensive_api_call",mock_get)
    async with AsyncClient(app=app, base_url=USERS_SERVICE_URL) as client:
        
        response = await client.get(f"{USERS_PREFIX}/time")
        assert response.status_code == 200
        assert response.json() == "hello_world"

