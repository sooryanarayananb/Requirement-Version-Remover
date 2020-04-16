# RVR (Requirement Version Remover)

RVR is a simple python script to remove all version details from requirements.txt file created in your project. 

The reason why I created this was, One of my office project was running in Python 2 and Django 1.11, and the project had more than 400 packages installed. The project needed to upgraded to latest version. So I had to create a new environment and updated it to latest packages. 

So RVR just generates a new requirements.txt file with all version details removed. 

#running the script generates requirements_new.txt file. 
###### python3 rvr.py requirements.txt 
