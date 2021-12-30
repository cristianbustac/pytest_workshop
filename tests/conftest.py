import asyncio
import os

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.config import Settings
from app.main import create_application

get_settings = Settings()




@pytest.fixture(scope="function", autouse=True)
def test_app():
    app = create_application()
    db_url = os.environ.get("sqlite://:memory:")
    initializer(["app.infra.postgres.models"], db_url="sqlite://:memory:", app_label="models")
    with TestClient(app) as test_client:
        yield test_client
    finalizer()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
