from math import exp

# def f1(x: float, u1: float, u2: float):
#     value = (u1 + 8 * u2) * (-1) 
#     return value

# def f2(x: float, u1: float, u2: float):
#     value = (-50) * u2
#     return value

# def f1_true(x: float):
#     value = (2 * exp(-1 * x) + exp((-50) * x)) / 3
#     return value

# def f2_true(x: float):
#     value = exp((-50) * x) * 2
#     return value

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

number_iter = 100
right_break = 0.1
# x_start = 0.0
# v1_start = 1.0
# v2_start = 2.0
x_start, v1_start, v2_start = 0.0, 7.0, 13.0
h = 0.001

def main():
    x_curr, v1_curr, v2_curr = x_start, v1_start, v2_start

    print("{0:4}|{1:5.5}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|".format("n", "Xn", "V1", "V2", "U1", "U2", "E1", "E2"))
    print("{0:4}|{1:5.5}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|".format(0, x_curr, v1_curr, v2_curr, 1, 2, 0, 0))

    for i in range(1, number_iter):
        if right_break <= x_curr:
            break
        x_next, v1_next, v2_next = rk2euler(x_curr, v1_curr, v2_curr, h)
        u1, u2 = calculate_true(x_next)
        print("{0:4}|{1:5.5}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|".format(i, x_next, v1_next, v2_next, u1, u2, (u1 - v1_next), (u2 - v2_next)))
        x_curr, v1_curr, v2_curr = x_next, v1_next, v2_next

if __name__ == "__main__":
    main()