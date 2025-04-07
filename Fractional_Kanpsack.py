def fKnapsack(w,v,cap):
    arr=[]
    for i in range(len(w)):
        ratio=v[i]/w[i]
        arr.append((ratio,w[i],v[i]))
    arr.sort(reverse=True)
    total_val=0
    for ratio,weight,value in arr:
        if weight<=cap:
            cap-=weight
            total_val+=value
        else:
            total_val+=(cap)*ratio
    return total_val

    
w = [10, 20, 30]
v = [60, 100, 120]
cap = 50

print(fKnapsack(w, v, cap))
 