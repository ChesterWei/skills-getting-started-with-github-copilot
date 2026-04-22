import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Shared TestClient fixture for all tests."""
    return TestClient(app)
