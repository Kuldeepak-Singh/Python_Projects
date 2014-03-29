''' How To Use : If a Source Directory is D:\\NewFolder\ABC_System\...
	then
	INPUT 1 (Enter File Name :)=> Name of the file for which diff directory is to be created
	INPUT 2 (Enter Source Directory Path )=> Path of the Source Directory (Example : D:\\NewFolder)
	INPUT 3 (Enter Destination Path :) => Path of the Destination Directory

	OUTPUT : Diff directory will be created at Destination Path if the file is found or Diff Directory is not already present in Destination Path
  
'''
import os
import sys
from os.path import join, getsize
print(__doc__)
filename=input('Enter File Name :')
sourcepath=input('Enter Source Directory Path :')
destinationpath=input ('Enter Destination Path :') 
filepath='a'
for root,dirs , files in os.walk(sourcepath):
#    print('printing root ',root)
    for name in files:
#       print('printing files',name)
        if filename in name:
            filepath = ''.join(root)
#            print(filepath)
            break
#    for dirt in dirs:
#        print('printing dirs',dirt)

try :
		temp = destinationpath +os.sep+'diff' +os.sep+'new'
		destination = filepath.replace(sourcepath,temp)
		os.makedirs(destination)
		explorenew = destination
		temp = destinationpath +os.sep+'diff' +os.sep + 'old'
		destination = filepath.replace(sourcepath,temp)
		os.makedirs(destination)
		exploreold = destination
		os.startfile(explorenew,'open')
		os.startfile(exploreold,'open')
		print("Difference Directory Successfully created")
except (FileExistsError , OSError):
				    print('Path Aleady Exists or File Not Found') 

