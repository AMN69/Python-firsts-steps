myfile = open('myfile.txt')
print(myfile.read())
print(myfile.read()) # here appears empty because the cursor is in the last line
myfile.seek(0)
print(myfile.read()) # here appears again the file from first line because we are puttin the cursor at the beginning
myfile.seek(0)
content = myfile.read()
print('content is: ', content)
myfile.seek(0)
print(myfile.readlines())
myfile.close()
with open('myfile.txt') as my_new_file: # not needed to close the file
    content2 = my_new_file.read()
print('from with: ', content2)
# write and overwrite files
with open('myfile.txt', mode='r') as myfile: # r = read, w = write, a = append, r+ = read/write, w+ = write/read
    contents3 = myfile.read()
print(contents3)
with open('my_new_file.txt', mode='r') as f:
    print('------')
    print(f.read())
with open('my_new_file.txt', mode='a') as f: # positions the cursor at the end
    print('------')
    f.write('\nFOUR ON FOURTH')
with open('my_new_file.txt', mode='r') as f:
    print('------')
    print(f.read())
myfile.close()
with open('notexitsfile.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')
