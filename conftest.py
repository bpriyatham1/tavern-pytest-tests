import pytest


@pytest.fixture
def admin_token():
    return "Basic YWRtaW46YWRtaW4xMjM="


@pytest.fixture
def peter_token():
    return "Basic cGV0ZXI6cGV0ZXIxMjM="
