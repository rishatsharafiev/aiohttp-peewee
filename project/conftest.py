import pytest

from project import settings
from project.application import init_app


@pytest.fixture
def test_app(loop):
    """Testing application"""
    settings.loop = loop
    settings.pool = settings.get_pool()
    settings.manager = settings.get_manager(settings.pool, settings.loop)

    return init_app(loop=loop)
