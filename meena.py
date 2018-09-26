textA ="apply"
textB ="apple"
print("textA:"+textA)
print("textB:"+textB)
result=" "
maxLen=len(textB)if len(textA)>len(textB) else len(textA)
for i in range(0,maxLen):
    if textA[i]!=textB[i]:
        break
    else:
        result+=textA[i]
        print(" longest common prefix '"+result+"'")
    
