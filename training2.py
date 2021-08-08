import matplotlib.pyplot as plt # for plotting
import numpy as np # for transformation

import torch # PyTorch package
import torchvision # load datasets
import torchvision.transforms as transforms # transform data
import torch.nn as nn # basic building block for neural neteorks
import torch.nn.functional as F # import convolution functions like Relu
import torch.optim as optim # optimzer


# python image library of range [0, 1] 
# transform them to tensors of normalized range[-1, 1]

transform = transforms.Compose( # composing several transforms together
    [transforms.ToTensor(), # to tensor object
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]) # mean = 0.5, std = 0.5

# set batch_size
batch_size = 4

# set number of workers
num_workers = 2


from labelbox import Project, Dataset, Client
from getpass import getpass
import os

#CRUD (CREATE READ UPDATE DESTROY) example 

# If you don't want to give google access to drive you can skip this cell
# and manually set `API_KEY` below.

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3MyMDZ6OXk0b244MHllajh3a3I0ZXI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3MyMDZ6OWg0b243MHllamcxMGQ5NWV4IiwiYXBpS2V5SWQiOiJja3MyajMwbGc2M2MwMHpkNTZ0bmFhdXozIiwic2VjcmV0IjoiMTc2OWEyODIzZDA4NTZkYTNhMDVlMGIyMTYyYzQ3MjciLCJpYXQiOjE2MjgzODYxNzMsImV4cCI6MjI1OTUzODE3M30.83cHXCRe227dqns_zdhqR7XcsFLY73hb-L7uBhXDJEk"
PROJECT_ID = "cks20zpo94sju0yejbghm0wr0"

ENDPOINT = "https://api.labelbox.com/graphql"

client = Client(api_key=API_KEY, endpoint=ENDPOINT)

project = client.get_project(PROJECT_ID)
dataset = next(project.datasets())

#read 
data_rows = dataset.data_rows()
data_row = next(data_rows)

#print("Associated dataset", data_row.dataset())
#print("Associated label(s)", next(data_row.labels()))
#print("External id", data_row.external_id)

data_row = dataset.data_row_for_external_id(data_row.external_id)
print(data_row)


trainset = data_row
trainloader = data_row
testset = data_row
testloader = data_row




# put 10 classes into a set
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck', 'fish')

#visualize 

def imshow(img):
  ''' function to show image '''
  img = img / 2 + 0.5 # unnormalize
  npimg = img.numpy() # convert to numpy objects
  plt.imshow(np.transpose(npimg, (1, 2, 0)))
  plt.show()

# get random training images with iter function


class Net(nn.Module):
    ''' Models a simple Convolutional Neural Network'''
	
    def __init__(self):
        super(Net, self).__init__()
	# 3 input image channel, 6 output channels, 
	# 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(3, 6, 5)
	# Max pooling over a (2, 2) window
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5) 
        self.fc1 = nn.Linear(16 * 5 * 5, 120)# 5x5 from image dimension
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
print(net)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)



"""
if __name__ == '__main__':
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)

    start.record()

    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

        # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    # whatever you are timing goes here
    end.record()

    # Waits for everything to finish running
    torch.cuda.synchronize()

    print('Finished Training')
    print(start.elapsed_time(end))  # milliseconds



    dataiter = iter(testloader)
    images, labels = dataiter.next()

    # print images
    imshow(torchvision.utils.make_grid(images))
    print('GroundTruth: ', ' '.join('%s' % classes[labels[j]] for j in range(4)))

    outputs = net(images)

    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join('%s' % classes[predicted[j]]
                              for j in range(4)))    


    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
        100 * correct / total))

"""

"""
if __name__ == '__main__':
	dataiter = iter(trainloader)
	images, labels = dataiter.next()

#error 

# call function on our images
	imshow(torchvision.utils.make_grid(images))

# print the class of the image
	print(' '.join('%s' % classes[labels[j]] for j in range(batch_size)))

"""





