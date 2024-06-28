def three_sum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []
    
    nums.sort()
    result = []
    
    for i, n in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i+1, len(nums)-1
        
        while l < r:
            summation = n + nums[l] + nums[r]
            if summation == 0:
                result.append([n, nums[l], nums[r]])
                
                # updating l and r pointers
                r -= 1
                l += 1
                
                # jump over duplicate value corresponding to r
                while nums[r] == nums[r+1] and l < r:
                    r -= 1
                # jump over duplicate values corresponding to l
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif summation < 0:
                l += 1
            elif summation > 0:
                r -= 1
                
    return result


