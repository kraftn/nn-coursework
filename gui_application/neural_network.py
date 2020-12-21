import torch


class RegressionNet(torch.nn.Module):
    def __init__(self, num_features):
        super(RegressionNet, self).__init__()
        self.fc1 = torch.nn.Linear(num_features, 500)
        self.act1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(500, 1)
        self.act2 = torch.nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.act2(x)
        return x