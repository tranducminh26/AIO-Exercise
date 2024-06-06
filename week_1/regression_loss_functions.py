import random
import math


def calc_loss():
    num_samples = input('Input number of samples (interger number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an interger number')
        return     
    num_samples = int(num_samples) 
    loss_name = input('Input loss name: ')
    predict = [random.uniform(0, 10) for _ in range(num_samples)]
    target = [random.uniform(0, 10) for _ in range(num_samples)]
    if loss_name == 'MAE':
        loss = [abs(y - y_hat) for y, y_hat in zip(target, predict)]
        final_loss = sum(loss)/num_samples
    elif loss_name == 'MSE':
        loss = [(y - y_hat)**2 for y, y_hat in zip(target, predict)]
        final_loss = sum(loss)/num_samples
    elif loss_name == 'RMSE':
        loss = [(y - y_hat)**2 for y, y_hat in zip(target, predict)]  
        final_loss = math.sqrt(sum(loss)/num_samples)
    else:
        print('Invalid loss name')
        return
    for i in range(num_samples):
        print(f'loss name : {loss_name}, sample : {i}, pred : {predict[i]}, target : {target[i]}, loss : {loss[i]}')
    print(f'final {loss_name}: {final_loss}')
    
    
calc_loss()
    
        
