import csv

with open('lab_11_data.csv','r') as f:
    f.readline()
    reader = csv.reader(f, delimiter=',')
    result=[]
    for row in reader:
        llist=[]
        x=len(row)
        for i in range(x-6):
            llist.append(row[i])
        result.append(llist)
    
    result1=[]
    for row in result:
        lis=[]
        for item in row:
            item = item.replace(",","")
            lis.append(item)
        result1.append(lis)
        
    # printing result 1
    # n = max(len(x) for l in result1 for x in l)
    # for row in result1:
    #     print(''.join(x.ljust(n + 2) for x in row)) 
    
    result2 = list(filter(lambda x: float(x[6]) >= -3, result1))
    # printing result 2
    # print("\n")
    # n = max(len(x) for l in result2 for x in l)
    # for row in result2:
    #     print(''.join(x.ljust(n + 2) for x in row))
    
    opn = list(map(lambda x: float(x[1]), result2))
    high = list(map(lambda x: float(x[2]), result2))
    low  = list(map(lambda x: float(x[3]), result2))
    
    opnAvg = sum(opn)/len(opn)
    highAvg = sum(high)/len(high)
    lowAvg = sum(low)/len(low)
    
    # print(opnAvg, highAvg, lowAvg)
    
    file3 = open("avg_output.txt", "w")
    file3.write("Open Average : " + str(opnAvg) + "\n")
    file3.write("High Average : " + str(highAvg) + "\n")
    file3.write("Low Average : " + str(lowAvg) + "\n")
    file3.close()
    
    print("Enter a character : ")
    ch = input()
    result4 = list(filter(lambda x: x[0][0] == ch, result2))
    
    if(len(result4) == 0):
        print("No result")
        file4 = open("stock_output.txt", "w")
        file4.write("No result")
        file4.close()
    else : 
        # printing result 4
        n = max(len(x) for l in result4 for x in l)
        for row in result4:
            print(''.join(x.ljust(n + 2) for x in row))
            
        file4 = open("stock_output.txt", "w")
        for row in result4:
            for item in row:
                file4.write(item + " ")
            print("\n")
        file4.close()

    
    
