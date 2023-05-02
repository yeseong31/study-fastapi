# CPU 바운드: 프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한됨을 의미한다.
def cpu_bound(number: int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
    return total


if __name__ == '__main__':
    result = cpu_bound(10)
    print(result)
