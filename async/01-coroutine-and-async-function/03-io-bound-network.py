import requests


# 네트워크 I/O 바운드
def io_bound_func():
    return requests.get("https://google.com")


if __name__ == "__main__":
    for _ in range(10):
        result = io_bound_func()
        print(result)
