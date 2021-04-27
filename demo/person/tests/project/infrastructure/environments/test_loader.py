
import pytest
from project.infrastructure.environments.loader import Configs


def test_loader_success():
    configs = Configs()
    assert configs.get_by_key("redis")


def test_loader_error_file():
    configs = Configs()
    assert pytest.raises(FileNotFoundError, configs.get_by_key, "security_token", "unknow_path")


def test_loader_error_config():    
    path = "./project/infrastructure/__init__.py"
    configs = Configs()
    assert pytest.raises(Exception, configs.get_by_key, "security_token", path)
