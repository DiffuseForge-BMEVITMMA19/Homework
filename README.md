# Homework: DiffuseForge
Homework repository for DiffuseForge team in BMEVITMMA19 (Deep Learning Class)

* Oravecz Márton Péter J38LZK
* Szimonenko Mikita Olekszijovics H8IUDR

## Milestone 1
The data we choose is the celebA and flowers102 datasets, which we download from kaggle using their API. We then use torch libraries to load and transform the data, then create a dataloader.

Task distribution:
* Szimonenko Mikita Olekszijovics: Data retrival and preparing 
* Oravecz Márton Péter: Infrastructure and Docker creation

### Files and their usage

* **data.ipynb**: Executable python notebook which contains the same steps as the two python file for easier iteration.
* **Dockerfile**: Description of the docker image. Planned updates: kaggle.json import as build argumentum
* **downloadKaggle.py**: Steps to download the datasets during Docker image creation.
* **preparations.py**: Steps to prepar dataset to follow-up steps.
* **README.md**: This file
* **runPreparation.sh**: Runs `preparation.py` and logs the result into `/output/output.log`.
* **config/requirements.txt**: Python dependency libraries declaration
* **config/kaggle.json**: Kaggle API key file. OVERWRITE THIS FILE BEFORE BUILDING THE IMAGE

Releveant folder in the containers:
* **/output/**: Output folder preferably mounted to a persistent volume.

### How to build and run the container

1. After registration at kaggle.com download the API key file and overwrite `config\kaagle.json` with it.
2. Run `docker build -t diffuseforge .` to build the image. It will take several minutes
3. Start a new container from the image with `docker run -it diffuseforge bash` in interactive mode.
4. Run Data preparation step with the following command: `./runPreparation.sh`. Logs are visible in the `/output/output.log` file.
