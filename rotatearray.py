class Rotation():
    def rotate(self, nums: list[int], k: int)-> None:
        k=k%len(nums)
        nums[:]=nums[-k:] + nums[:-k]

nums=[1,3,5,7,9]
k=9
answer=Rotation()
answer.rotate(nums,k)
print(nums)
