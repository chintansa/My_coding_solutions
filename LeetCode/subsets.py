nums =[1,2,3]

subset =[[],[nums[0]]]



for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)+1):
            s = [nums[i]]+ nums[j:k]
            if nums[j:k] not in subset:
                subset.append(nums[j:k])
            if s not in subset:
                subset.append(s)    

print(subset)                