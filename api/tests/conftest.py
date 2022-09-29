from dotenv import load_dotenv


def pytest_sessionstart():
    load_dotenv()
