def reversePairs(nums):
    li=[]
    n=len(nums)
    for i in nums:
        for j in range(n-1,i,-1):
            if(nums[i]>2*nums[j]):
                li.append([nums[i],nums[j]])
    print(li)
    return len(li)

nums =[2,4,3,5,1]