import math


# Exercise 1
def calc_f1_score(tp ,fp ,fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

assert round (calc_f1_score(tp=2, fp=3, fn=5) , 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))


#Exercise 2
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))


#Exercise 4
def calc_sig(x):
    return 1 / (1 + math.exp(-x))

assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))


#Exercise 5
def calc_elu(x):
    alpha = 0.01
    if x <= 0:
        result = alpha * (math.exp(x) - 1)
    else:
        result = x
    return result

assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))


#Exercise 6
def calc_relu(x):
    result = 0
    if x >0:
        result = x
    return result


def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return calc_sig(x)
    if act_name == 'relu':
        return calc_relu(x)
    if act_name == 'elu':
        return calc_elu(x)

assert calc_activation_func(x = 1, act_name = 'relu') == 1
print(round(calc_activation_func(x = 3, act_name = 'sigmoid'), 2))


#Exercise 7
def calc_ae(y, y_hat):
    return abs(y - y_hat)

y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))


#Exercise 8
def calc_se(y, y_hat):
    return (y - y_hat) ** 2

y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))


#Exercise 9
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i))/fact(2*i)
    return result

assert round(approx_cos(x = 1, n = 10), 2) == 0.54
print(round(approx_cos(x = 3.14, n = 10), 2))


#Exercise 10
def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i+1))/fact(2*i+1)
    return result

assert round(approx_sin(x = 1, n = 10), 4) == 0.8415
print(round(approx_sin(x = 3.14, n = 10), 4))


#Exercise 11
def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i+1))/fact(2*i+1)
    return result

assert round(approx_sinh(x = 1, n = 10), 2) == 1.18
print(round(approx_sinh(x = 3.14, n = 10), 2))
    

#Exercise 12
def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i))/fact(2*i)
    return result

assert round(approx_cosh(x = 1, n = 10), 2) == 1.54
print(round(approx_cosh(x = 3.14, n = 10), 2))   