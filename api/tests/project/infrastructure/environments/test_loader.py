
import pytest
from project.infrastructure.environments.loader import Configs


def test_loader_success():
    configs = Configs()
    if not configs.get_by_key("redis"):
        raise AssertionError


def test_loader_error_file():
    configs = Configs()
    if not pytest.raises(FileNotFoundError, configs.get_by_key, "security_token", "unknow_path"):
        raise AssertionError


def test_loader_error_config():    
    path = "./project/infrastructure/__init__.py"
    configs = Configs()
    if not pytest.raises(Exception, configs.get_by_key, "security_token", path):
        raise AssertionError
