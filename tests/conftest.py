"""Test configuration for Log Analysis Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "log-analysis-agent", "category": "DevOps & Platform Engineering"}
