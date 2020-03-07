import myme_models as models
import myme_load as txt

epoch = 1000
out_dim = 114514
BATCH_SIZE = 256

net = models.Model00(256, 5, out_dim)
param = net.parameters()
net.cpu()
f_loss= nn.MSELoss()
# optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
optimizer = optim.Adam(net.parameters(), lr=0.001)

for i in range(epoch):
    optimizer.zero_grad()
    output = net(x)
    loss = f_loss(output, y)
    loss.backward()
    optimizer.step()
    print(loss.item())
torch.save(net.state_dict(), "./result/model.npz")