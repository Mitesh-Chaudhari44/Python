line_count = 0
f = open('file.txt', 'r')
for line in f:
    line_count += 1
    
f.close()
print("The file has line_count : " , line_count)

