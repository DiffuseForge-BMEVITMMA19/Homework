import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
print("transformation created")
print(transform)
dataset = datasets.ImageFolder(root="./data/celeba/img_align_celeba/", transform=transform)
print("dataset created")
print(dataset)
batch_size = 64
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
print ("Dataloader crated")