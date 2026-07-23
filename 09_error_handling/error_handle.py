file = open('youtube.txt', 'w')
# if opening a file directly without creating it without using 'w' it will give error
# whereas if opened with file name and 'w', then it creates the file in write mode.

try:
    file.write("Python coding practice")

finally:
    file.close()
# previous method of opening a file, writing in it and then manually closing the file.

with open('youtube.txt', 'w') as file:
    file.write('Python coding practice')
# new clean method to open and write in a file. no manual closing of file.

