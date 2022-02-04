class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) 
{
        nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
        if(nums.size() == 1)
            return 1;
        int rlt = 2;
        for(int i=1; i<nums.size()-1; ++i)
        {
            if(nums[i-1] < nums[i] and nums[i+1] < nums[i] or
               nums[i-1] > nums[i] and nums[i+1] > nums[i])
                ++rlt;
        }
        return rlt;
}
};