def threeSum(nums:list)->list:
    nums.sort()
    result = []
    for i, number in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        if len(nums) <= 2:
            return 'Array Input Length Must More Than 2'
        elif i == right:
            break
        while nums[left] + nums[right] + nums[i] == 0 or nums[left] < nums[right]:
            if(nums[left] + nums[right] + number == 0):
                answer = [number,nums[left],nums[right]]
                if answer not in result:
                    result.append(answer)
                break
            elif(nums[left] + nums[right] + number  < 0):
                left += 1
            else:
                right -= 1
    return result

nums = [int(x) for x in input('Enter Your List : ').split()]
print(threeSum(nums))