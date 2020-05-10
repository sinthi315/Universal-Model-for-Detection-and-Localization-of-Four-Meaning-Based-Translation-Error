import string

f = open('datas.txt', 'r').readlines()

for line in f:
    if line[0:3] == 'ENG':
        source_segment = open("source_segment.txt", 'a')
        source_segment.write(line)
        source_segment.close() 
    elif line[0:3] == 'FRA':
        target_segment = open("target_segment.txt", 'a')
        target_segment.write(line)
        target_segment.close()
    else:
        print(" ")


            
        
