
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor


def test_basics_01_quickstart() -> None:
    # Download test data from open datasets.
    test_data = datasets.FashionMNIST(
        root='data',
        train=False,
        download=True,
        transform=ToTensor(),
    )

    batch_size = 64

    # Create data loaders.
    test_dataloader = DataLoader(test_data, batch_size=batch_size)

    for X, y in test_dataloader:
        print(f'Shape of X [N, C, H, W]: {X.shape}')
        print(f'Shape of y: {y.shape} {y.dtype}')
        break
