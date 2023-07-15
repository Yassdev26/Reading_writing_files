#  -----------------------------------------------
#  ------- File Handling => Read File ------------
#  -----------------------------------------------

#  -----------------------------------------------
#  ------- /1/ File Data Object  -----------------
#  -----------------------------------------------

My_Files = open("file","r") #file for mac / file.txt

print(My_Files)
print(My_Files.name) 
print(My_Files.mode)
print(My_Files.encoding)

print(My_Files.read())
My_Files.close() #close the file
