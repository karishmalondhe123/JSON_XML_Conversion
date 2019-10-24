Purpose of the project:

JSON2XMLEncrypt.py script will take all the json files located in the current directory by looking for the extensions as “.json” as an input. These files will be converted into the xml files and will be then encrypted.  

Decrypt_XML.py script will take the output of first python scripts i.e. the encrypted xmls as its input and will convert these into a decrypted form.

The docker-compose.yml file is used to transfer the output of first python script i.e. the encrypted xmls to make them as an input file to the second python script where the encrypted xmls are decrypted. This is done by volume mounts with docker compose. 


Installations: 
• Docker Version 18.06.1-ce.
• Python 3.4.2
• docker-compose version 1.24.1
• OS used by me -- ec2 instance -linux


Commands and steps to execute this project:
1. Change the directory to the parent folder where .yml and two folders are present.
2. Execute : docker volume create jsontoxmlvolume
3. Execute : docker volume create xmldecryptvolume
4. Execute : docker-compose build
5. Execute : docker-compose up service_encrypt
6. Execute : docker-compose up service_decrypt# JSON_XML_Conversion
