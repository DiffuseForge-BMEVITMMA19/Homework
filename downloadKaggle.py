import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files("jessicali9530/celeba-dataset", path="./data/celeba/", unzip=True)
kaggle.api.dataset_download_files("demonplus/flower-dataset-102", path="./data/", unzip=True)