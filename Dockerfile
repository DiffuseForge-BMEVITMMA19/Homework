FROM python:3.8

COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install nano
RUN mkdir /root/.config &&\ 
	mkdir /root/.config/kaggle/ &&\
	mkdir ./data &&\ 
	mkdir /output &&\ 
	mkdir /app/data/celeba &&\ 
	mkdir ./data/flowers102/
RUN cp config/kaggle.json /root/.config/kaggle/ 
RUN pip install -r config/requirements.txt
RUN python downloadKaggle.py
RUN chmod u+x runPreparation.sh
RUN tar -xvzf ./data/102flowers.tgz -C ./data/flowers102/