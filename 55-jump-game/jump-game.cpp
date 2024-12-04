class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        int max = 0;
        
        while (i < n) {
            // If current index is beyond the maximum reach, return false
            if (i > max) return false;
            
            // Update the maximum reachable index
            if (i + nums[i] > max) max = i + nums[i];
            
            // If the max reach is beyond or equal to the last index, return true
            if (max >= n - 1) return true;
            
            i++;
        }
        
        return false;
    }
};