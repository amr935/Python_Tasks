a=input("Enter text to write to the file:")

file_3=open('output.txt','w')
writing_file=file_3.write(a)
file_3.close()

print('Data successfully written to output.txt.')

b=input("Enter additional text to append:")

file_3=open('output.txt','a')
appending_file=file_3.write('\n'+b)
file_3.close()

print('Data successfully appended.')


print('Final content of output.txt:')

file_3=open('output.txt','r')
appending_file=file_3.read()
print(appending_file)
file_3.close()