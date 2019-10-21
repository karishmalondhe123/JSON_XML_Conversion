FROM python:3.4.2
RUN pip install json2xml
RUN pip install xmltodict
WORKDIR /home
RUN mkdir XMLFileInput
RUN mkdir Outpufiles
RUN mkdir Outpufiles/XMLFileDecryptedOutput
COPY Decrypt_XML.py ./
CMD ["python", "Decrypt_XML.py"]
