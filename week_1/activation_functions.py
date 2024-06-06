import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    result = 0
    if x > 0:
        result = x
    return result


def elu(x):
    result = 0
    alpha = 0.01
    if x <= 0:
        result = alpha * (math.exp(x) - 1)
    else:
        result = x
    return result


def calc_activation_func():
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    act_name = input("Input activation Function (sigmoid|relu|elu): ").lower()
    if act_name == 'sigmoid':
        print(f"{act_name}: f({x}) = {sigmoid(x)}")
    elif act_name == 'relu':
        print(f"{act_name}: f({x}) = {relu(x)}")
    elif act_name == 'elu':
        print(f"{act_name}: f({x}) = {elu(x)}")
    else:
        print(f"{act_name} is not supported")


calc_activation_func()
