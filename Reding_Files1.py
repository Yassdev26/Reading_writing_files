#  -----------------------------------------------
#  ------- File Handling => Read File ------------
#  -----------------------------------------------

#  -----------------------------------------------
#  ------- /1/ File Data Object  -----------------
#  -----------------------------------------------
print(myFile)
print(myFile.name) 
print(myFile.mode)
print(myFile.encoding)

My_Files = open("file","r") #file for mac / file.txt
print(My_Files.read())
My_Files.close() #close the file
