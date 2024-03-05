from app.main import app
from fastapi.testclient import TestClient
import pytest
import warnings

# Deactivate all warnings
warnings.simplefilter("ignore")


@pytest.fixture(scope='module')
def test_app():
    client = TestClient(app)
    yield client
