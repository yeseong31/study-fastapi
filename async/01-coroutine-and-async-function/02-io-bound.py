# I/O 바운드: 프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미한다.
def io_bound_func():
    print("값을 입력해 주세요.")
    return int(input()) + 100


if __name__ == "__main__":
    result = io_bound_func()
    print(result)
