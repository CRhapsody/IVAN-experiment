import torch
import torch.nn as nn
import torch.nn.functional as F
# from auto_LiRPA import PerturbationLpNorm, BoundedParameter


# class Acasxu_net(nn.Module):
#     def __init__(self, in_dim = 5, out_dim = 5):
#         super(Acasxu_net, self).__init__()
#         self.fc1 = nn.Linear(in_dim, 50)
#         self.fc2 = nn.Linear(50, 50)
#         self.fc3 = nn.Linear(50, 50)
#         self.fc4 = nn.Linear(50, 50)
#         self.fc5 = nn.Linear(50, 50)
#         self.fc6 = nn.Linear(50, 50)
#         self.fc7 = nn.Linear(50, out_dim)

#     def forward(self, x):
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = F.relu(self.fc3(x))
#         x = F.relu(self.fc4(x))
#         x = F.relu(self.fc5(x))
#         x = F.relu(self.fc6(x))
#         x = self.fc7(x)
#         return x

class Acasxu_net(nn.Module): 
    def __init__(self, net_dims, activation=nn.ReLU):
        super().__init__()
        
        self.net_dims=net_dims
        self.layers = nn.ModuleList()
        for i in range(len(net_dims) - 1):            
            self.layers.append(nn.Linear(net_dims[i], net_dims[i + 1]))

            # use activation function if not at end of layer
            if i != len(net_dims) - 2:
                self.layers.append(activation())

    def forward(self, x):     #forward propagate        
        # x = x.reshape(-1,self.net_dims[0])        
        for i, layer in enumerate(self.layers):            
            x = layer(x)            
        return x

    def transfer(self,layer_index, add_w,add_b):
        self.layers[layer_index].weight = torch.nn.Parameter(add_w)
        self.layers[layer_index].bias = torch.nn.Parameter(add_b)


