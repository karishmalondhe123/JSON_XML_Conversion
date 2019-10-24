#######################################################################################
#Purpose: This script will be executed using a Dockerfile stored at the same folder. Convert all the json files into XML and encrypt the same.
#The output of these files (i.e. Encrypted-XML) will be stored in the first container and will be transferred to another container using volume mounts with docker compose.
#Created By: Karishma Londhe (londhe.karishma61@gmail.com)
#######################################################################################

## Import the required libraries
from json2xml import json2xml, readfromurl, readfromstring, readfromjson
import os
import sys
import json
from json import loads
import xmltodict
import base64

#Create a list to save all the files with .json ext within the directory
lJSONExtFiles = []
sCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
sNewDirForEncryptFiles = "EncryptedFiles/XMLFileEncryptedOutput"

for root, dirs, files in os.walk(sCurrentDirectory):
	for file in files:
		if file.endswith(".json"):
			sJsonFileNames = os.path.join(root, file)
			lJSONExtFiles.append(sJsonFileNames)

#Iterate through all the .json files to convert in xml and encrypt the same			
for sFiles in lJSONExtFiles:
	#Replace "/" with the "\" 
	replaced_filename = sFiles.replace("/", "\\")

	#Get only the file name
	sOnlyFileName = str(replaced_filename.split("\\",-1)[-1]).replace(".json","")
	
	#Read the .json file
	with open(sFiles, 'r') as f:
		jsonString = f.read()
	
	#Convert it into .xml file
	
	xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
	
	print("File "+str(sOnlyFileName)+ " is converted into .xml format.\n")
	#Write it in a new file
	with open(str(sNewDirForEncryptFiles)+"/"+str(sOnlyFileName)+'.xml', 'w') as sNewfile:
		
		sNewfile.write(xmlString)
	sNewfile.close()
	
	#Encrypt the .xml file and re-write within the same file
	xmlEncrypt = open(str(sNewDirForEncryptFiles)+"/"+str(sOnlyFileName)+'.xml',"rb").read()
	sEncodedStructure = base64.b64encode(xmlEncrypt).decode('utf-8')
	
	with open(str(sNewDirForEncryptFiles)+"/"+str(sOnlyFileName)+'.xml', 'w') as sNewEncryptedfile:
		
		sNewEncryptedfile.write(sEncodedStructure)
	print("File "+str(sOnlyFileName)+ " is encrypted.\n")
