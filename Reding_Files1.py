#  -----------------------------------------------
#  ------- /1/ File Data Object  -----------------
#  -----------------------------------------------


print(My_Files)
print(My_Files.name) 
print(My_Files.mode)
print(My_Files.encoding)

#  ---------------------------------------------------------
#  ---/ r / ---> /2/ File Handling => Read File ------------
#  ---------------------------------------------------------

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

#r+ => You can read the file and also write to it ...
#  ------------------------------------------------------------------------
#  ---/ r+ / ---> /2/ File Handling => Read File & Write to it ------------
#  ------------------------------------------------------------------------

My_Files = open("write_r+","r+")
print(My_Files.write("She is my mother."))
My_Files.close()


My_Files.close() #close the file
