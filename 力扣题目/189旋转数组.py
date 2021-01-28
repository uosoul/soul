class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def swap(l,r):
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        swap(0,n-k-1)
        swap(n-k,n-1)
        swap(0,n-1)

