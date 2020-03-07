import torch
import torch.nn as nn

# model0 using LSTM

class Model00(nn.Module):
    '''
    input layer : 256 default
    hidden layer : 5 default
    '''
    def __init__(self, input_dim=256, hidden_dim=5, output_dim):
        super(Model00, self).__init__()

        self.rnn = nn.LSTM(input_size = input_dim,
                            hidden_size = hidden_dim,
                            batch_first = True)
        self.output_layer = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, inputs, hidden0=None):
        output, (hidden, cell) = self.rnn(inputs, hidden0)  #LSTM
        output = self.output_layer(output[:, -1, :])        #全結合層
        return output

# model1 using back foward
class Model01(nn.Module):
    def __init__(self, input_dim=256, output_dim):
        super(Net4Iris, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(16, output_dim)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.sigmoid(self.fc3(x))
        return x


# class Model02(nn.Module):
#     def __init__(self, input_dim=256, output_dim):
#         super(Net4Iris, self).__init__()
#         self.fc1 = nn.Linear(input_dim, 128)
#         self.fc2 = nn.Linear(128, 64)
#         self.fc3 = nn.Linear(16, output_dim)
        
#     def forward(self, x):
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = F.sigmoid(self.fc3(x))
#         return x