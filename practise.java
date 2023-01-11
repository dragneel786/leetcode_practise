import java.util.*;
class Solution {
    public static void main(String args[]){
        Solution s = new Solution();
        int target = 9;
        int nums[] = {2,7,11,15};
        for(int i: s.twoSum(nums, target)){
            System.out.println(i);
        }
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hmap = new HashMap<>();
        for(int i  = 0; i < nums.length; i++){
            Integer val = hmap.get(target - nums[i]);
            if(val != null){
                return (new int[]{val, i});
            }
            hmap.put(nums[i], i);
        }
        return new int[2];
    }
}