class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1

        ownership_set = set()

        for i in nums:
            if i in ownership_set:
                return True
            ownership_set.add(i)
        return False
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        
        for key, value in s_dict.items():
            for key_1, value_1 in t_dict.items():
                if key not in t_dict:
                    return False
                if key_1 not in s_dict:
                    return False
                if s_dict[key] != t_dict[key]:
                    return False
            
        return True

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = defaultdict(lambda:-1)
        for i in range(len(nums)):
            if nums_dict[target-nums[i]] != -1:
                return[nums_dict[i], i] 
            else:
                nums_dict[nums[i]] = i
        
        

                
                

        


        
        

        



        