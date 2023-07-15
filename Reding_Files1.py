#  -----------------------------------------------
#  ------- /1/ File Data Object  -----------------
#  -----------------------------------------------


print(My_Files)
print(My_Files.name) 
print(My_Files.mode)
print(My_Files.encoding)

#  -----------------------------------------------
#  ------- /2/ File Handling => Read File ------------
#  -----------------------------------------------

My_Files = open("file","r") #file for mac / file.txt for windows

print(My_Files.read())

print(My_Files.readline(5))
print(My_Files.readline())
print(My_Files.readline())


print(My_Files.readlines())
print(My_Files.readlines(50))
print(type(My_Files.readlines()))


# => I will give you example about for loops with reading files
for line in myFile:
    print(line)
    if line.startswith("Islam he's from egypt"):
        break





My_Files.close() #close the file
