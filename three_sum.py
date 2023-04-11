from typing import List


def threeSum(nums: List[int], target: int) -> List[List[int]]:
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = [i]
        else:
            hashmap[nums[i]].append(i)

    nums.sort()
    res = []
    for i in range(len(nums)):
        s = set()
        current = target - nums[i]
        for j in range(i + 1, len(nums)):
            if current - nums[j] in hashmap and i != j:
                if (current - nums[j]] == nums[i] and len(hashmap(nums[i])) > \
                        1) or (current - nums[j] == nums[j] and len(hashmap(\
                        nums[j]) > 1)) or
                res.append([nums[i], nums[j], current - nums[j]])
                print(res)

    return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums, 0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
