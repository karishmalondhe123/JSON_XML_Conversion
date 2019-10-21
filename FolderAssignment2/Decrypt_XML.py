## Import the required libraries
import json
import os
import xmltodict
import base64

#Create a list to save all the files with .xml ext within the directory
#and which are the output of encrypted script
lXMLExtFiles = []
sCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
sXMLEncryptInput = "XMLFileInput"
sNewDirForDecryptFiles = "Outpufiles/XMLFileDecryptedOutput"

for root, dirs, files in os.walk(sXMLEncryptInput):
	for file in files:
		if file.endswith(".xml"):
			sXMLFileNames = os.path.join(root, file)
			lXMLExtFiles.append(sXMLFileNames)

#Iterate through all the .json files to convert in xml and encrypt the same			
for sFiles in lXMLExtFiles:
	#Replace "/" with the "\" 
	replaced_filename = sFiles.replace("/", "\\")

	#Get only the file name
	sOnlyFileName = str(replaced_filename.split("\\",-1)[-1])
	
	#Read the .xml file to decrypt the code
	with open(str(sXMLEncryptInput)+"/"+sOnlyFileName, 'rb') as f:
		xmlEncrypt = f.read()
		sDecodedStructure = base64.b64decode(xmlEncrypt).decode('utf-8')
		
	
	#Write the decrypted code
	with open(str(sNewDirForDecryptFiles)+"/Decrypt_"+sOnlyFileName, 'w') as sDecryptedfile:
		sDecryptedfile.write(sDecodedStructure)
		print("File Decrypt_"+sOnlyFileName+ "is decrypted.\n")
	sDecryptedfile.close()
