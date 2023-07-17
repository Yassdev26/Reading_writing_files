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

My_Files = open("Read","r") #file for mac / file.txt for windows

print(My_Files.read())
#readline / readlines
print(My_Files.readline(5))
print(My_Files.readline())
print(My_Files.readline())
print(My_Files.readlines())
print(My_Files.readlines(50))
print(type(My_Files.readlines()))


# => I will give you example about for loops with reading files
for line in myFile:
    print(line)
    if line.startswith("Tomorrow I will go to Morocco"):
        break


#r+ => You can read the file and also write to it ...
#  ------------------------------------------------------------------------
#  ---/ r+ / ---> /3/ File Handling => Read File & Write to it ------------
#  ------------------------------------------------------------------------
#YOU CAN READ THE FILE AND ALSO WRITE TO IT ...

My_Files = open("Read","r+")
print(My_Files.write("She is my mother."))


#  --------------------------------------------------------------------------------------------------------------------
#  ---/ w / ---> /4/ File Handling => Delete the things that were in a file & add the things you are going to write ---
#  --------------------------------------------------------------------------------------------------------------------
#DELETE THE THINGS THAT WERE IN A FILE & ADD THE THINGS YOU ARE GOING TO WRITE ...

My_Files = open("write","w")
print(My_Files.write("She is my mother."))


#  ---------------------------------------------------------------------------------------------------------------------
#  ---/ w+ / ---> /5/ File Handling => Delete the things that were in a file & add the things you are going to write ---
#  ---------------------------------------------------------------------------------------------------------------------
#The difference between w and w + is that in w + a file can be created for you if you do not write any existing file, meaning when you write inside a file that does not exist on a project, it can be added while maintaining the same properties of w

My_Files = open("write","w+")
print(My_Files.write("The cat curled up on the cozy blanket and purred contentedly."))


#  ---------------------------------------------------------------------------------------------------
#  ---/ a / ---> /6/ File Handling => You can write to a file without deleting the previous write ----
#  ---------------------------------------------------------------------------------------------------
#YOU CAN WRITE TO A FILE WITHOUT DELETING THE PREVIOUS WRITE ...

My_Files = open("write","a")
print(My_Files.write("The sun rises in the east and sets in the west."))


#  ----------------------------------------------------------------------------------------------------
#  ---/ a+ / ---> /7/ File Handling => You can write to a file without deleting the previous write ----
#  ----------------------------------------------------------------------------------------------------
# a+ like  w / w+ / a / a+  ( You can write to a file without deleting the previous write ).

My_Files = open("write","a")
print(My_Files.write("I love the smell of freshly baked bread in the morning."))



My_Files.close() #Close The File
