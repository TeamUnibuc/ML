import torch as th
import torch.nn as nn
import matplotlib.pyplot as plt

def GetRandomSnake():
    return None

def Evolve(snake : torch.nn.modules.container.Sequential, GENERATION : int):
    return [None]







### OLD
model = nn.Sequential(
    nn.Linear(N, 1)
).cuda()

def frwd_pass(fin):
    return model(fin.cuda())

def train(fin : th.Tensor, fout : th.Tensor, epoch, lr):
    adam = th.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.L1Loss()

    loss_history = []

    for i in range(epoch):
        adam.zero_grad()
        rez = model(fin.cuda())
        loss = loss_fn(fout, rez.cpu())
        loss.backward()
        loss_history.append(loss)
        adam.step()
        if i % 100 == 0:
            print("Epoch #", i)

    plt.plot(loss_history)
    plt.show()
