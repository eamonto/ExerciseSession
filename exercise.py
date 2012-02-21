'''
In this file is do the python exercise
'''

import io, glob, os, math

os.system("ls cleandata > input.dat")

f = open('input.dat', 'r')

aux = True
count = 0
while aux == True :
    count += 1
    if f.readline()=='': aux = False

f.close()

filek = range(0,count)

f = open('input.dat', 'r')

count = 0
for line in f:
    filek[count] = open('cleandata/'+line.split()[0],'r')
    count += 1


for j in range(0,9):
    aux_line = filek[0].readline()

    answer = False
    flag = False
    for i in range(0,len(aux_line)-1):
        if aux_line[i]=='#': answer = True
        if flag == True and aux_line[i]!=' ':
            answer = True

        if aux_line[i-1]==':' and aux_line[i]==' ':
            flag = True

    print answer


            
'''
aux = True
count = 0
while aux == True :
    if aux_line[count]=='':
        aux = False
        print "finish"
    count += 1

print aux_line[1]
'''
#print count

#file = range(0,count)

#print file





#print test

#for i in range(0,10):
#print files

'''
def find_create_list:
''' 

    
