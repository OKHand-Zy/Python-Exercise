# -*- coding: utf-8 -*-

'''

    #Gossiping-QA-Dataset.txt
with open("D:\\UC\\test\\Gossiping-QA-Dataset.txt","r",encoding="utf-8") as f:
    sum=0
    data=[]
    score=[]
    for line in f:
        for a in line:
            if a != " " and a !="	" and a != "\n" :
                sum=sum+1 
                data.append(a)                
    data_cont = set(data)
    data_cont = list(data_cont)    
    #找字跟次數放入score
    for i in range(len(data_cont)):
        set = data.count( str(data_cont[i] ) ) 
        score.append( (data_cont[i],set) )
    #排好順序放入score_s
    score_s = sorted(score, key=lambda x: x[1] , reverse=True)

f.close()
#輸出
print(f"總字元數 : {sum}")
print(f"總單字詞數 : {len(data_cont)}")
for j in range(len(score_s)):
    print(f"{score_s[j][0]} : {score_s[j][1]}")

'''

with open("D:\\UC\\test\\Gossiping-QA-Dataset.txt","r",encoding="utf-8") as f:
    sum=0
    data={}
    for line in f:
        for a in line:
            if a != " " and a !="	" and a != "\n" :
                sum=sum+1 
                if a in data :
                    data[a]+=1
                else:
                    data[a]=1
score_s = sorted(data.items(), key=lambda x: x[1] , reverse=True)
f.close()

file = open("D:\\UC\\test\\123.txt","w",encoding="utf-8")
file.write("總字元數 : " + str(sum) +"\n" )
file.write("總單字詞數 : " + str( len(score_s) ) +"\n")
for i in range(len(score_s)):
    file.write(str(score_s[i][0])+" : "+str(score_s[i][1]) +"\n")
file.close()
print("OK!")

