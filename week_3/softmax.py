import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdims=True)
        return x_exp / total
    
    
class Softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        total = x_exp.sum(0, keepdims=True)
        return x_exp / total