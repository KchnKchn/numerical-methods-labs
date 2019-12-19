from math import exp

def f1(x: float, u1: float, u2: float):
    value = -500.005 * u1 + 499.995 * u2
    return value

def f2(x: float, u1: float, u2: float):
    value = 499.995 * u1 - 500.005 * u2
    return value

def f1_true(x: float):
    value = 10 * exp(-0.01 * x) - 3 * exp(-1000 * x)
    return value

def f2_true(x: float):
    value = 10 * exp(-0.01 * x) + 3 * exp(-1000 * x)
    return value

def calculate_true(x: float):
    return f1_true(x), f2_true(x)

def rk2euler(x_curr: float, v1_curr: float, v2_curr: float, h: float):
    x_euler = x_curr + h
    v1_euler = v1_curr + h * f1(x_curr, v1_curr, v2_curr)
    v2_euler = v2_curr + h * f2(x_curr, v1_curr, v2_curr)

    x_next = x_euler
    v1_next = v1_curr + 0.5 * h * (f1(x_curr, v1_curr, v2_curr) + f1(x_euler, v1_euler, v2_euler))
    v2_next = v2_curr + 0.5 * h * (f2(x_curr, v1_curr, v2_curr) + f2(x_euler, v1_euler, v2_euler))
    return x_next, v1_next, v2_next

def print_header():
    print("|Итерация |Время     |Численное решение                                  |Точное решение                                     |Глобальная погрешность                             |")
    print("|---------|----------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|")
    print("|{0:9}|{1:10.5}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|".format("n", "Xn", "V1", "V2", "U1", "U2", "E1", "E2"))

def print_string(iter: int, x: float, v1: float, v2: float, u1: float, u2: float, e1: float, e2: float):
    print("|{0:9}|{1:10.5}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|".format(iter, x, v1, v2, u1, u2, e1, e2))

def print_table(x_list: list, v1_list: list, v2_list: list, u1_list: list, u2_list: list):
    print_header()
    number_iters = len(x_list)
    if number_iters < 150:
        for i in range(number_iters):
            print_string(i, x_list[i], v1_list[i], v2_list[i], u1_list[i], u2_list[i], u1_list[i] - v1_list[i], u2_list[i] - v2_list[i])
    else:
        for i in range(101):
            print_string(i, x_list[i], v1_list[i], v2_list[i], u1_list[i], u2_list[i], u1_list[i] - v1_list[i], u2_list[i] - v2_list[i])
        for i in range(30, 0, -1):
            print_string(number_iters - i, x_list[-i], v1_list[-i], v2_list[-i], u1_list[-i], u2_list[-i], u1_list[-i] - v1_list[-i], u2_list[-i] - v2_list[-i])

def calculate(x_start: float, v1_start: float, v2_start: float, h_start: float, epsilon: float):
    x_list = [x_start]
    v1_list = [v1_start]
    v2_list = [v2_start]
    u1_list = [v1_start]
    u2_list = [v2_start]

    x_curr, v1_curr, v2_curr, h = x_start, v1_start, v2_start, h_start
    for i in range(1, number_iter + 1):
        if right_break <= x_curr:
            break
        while(True):
            x_next, v1_next, v2_next = rk2euler(x_curr, v1_curr, v2_curr, h)
            x05, v1_05, v2_05 = rk2euler(x_curr, v1_curr, v2_curr, h / 2)
            _, v12, v22 = rk2euler(x05, v1_05, v2_05, h / 2)
            e = max(abs(v1_next - v12), abs(v2_next - v22)) / 3
            if epsilon < e:
                h /= 2
                continue
            if epsilon / 3 <= e <= epsilon:
                break
            if e < epsilon / 3:
                h *= 2
                break
        u1, u2 = calculate_true(x_next)
        x_curr, v1_curr, v2_curr = x_next, v1_next, v2_next
        x_list.append(x_curr)
        v1_list.append(v1_curr)
        v2_list.append(v2_curr)
        u1_list.append(u1)
        u2_list.append(u2)
    return x_list, v1_list, v2_list, u1_list, u2_list

number_iter = 250000
right_break = 500
x_start, v1_start, v2_start = 0.0, 7.0, 13.0
h_start = 0.01
epsilon = 0.0000001

def main():
    print_table(*calculate(x_start, v1_start, v2_start, h_start, epsilon))

if __name__ == "__main__":
    main()
