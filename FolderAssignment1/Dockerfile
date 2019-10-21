FROM python:3.4.2
RUN pip install json2xml
RUN pip install xmltodict
WORKDIR /home
RUN mkdir EncryptedFiles
RUN mkdir EncryptedFiles/XMLFileEncryptedOutput
COPY JSON2XMLEncrypt.py ./
COPY *.json ./
CMD ["python", "JSON2XMLEncrypt.py"]
