from .base import engine 


def wait_unlesss_db_started() -> None:
    connected = False
    while not connected:
        if database_started():
            print("----------------------------------------")
            connected = True


def database_started() -> bool:
    try:
        engine.connect()
        return True
    except RuntimeError as e:
        print(e)
        return False
