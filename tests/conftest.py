"""Shared pytest fixtures for the FastAPI backend tests."""

import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # activities is a module-level dict mutated in-place by the endpoints
    original_state = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
