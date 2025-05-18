file_2=open('sample.txt','r')
reading_file=file_2.read()
print(reading_file)
file_2.close()
#Let sample1.txe file does not exit, for this the error handling would be like:
try:
    file_2 = open('sample1.txt', 'r')
    reading_file = file_2.read()
    print(reading_file)
    file_2.close()
except FileNotFoundError:
    print("Error:The file 'sample1.txt' was not found")
