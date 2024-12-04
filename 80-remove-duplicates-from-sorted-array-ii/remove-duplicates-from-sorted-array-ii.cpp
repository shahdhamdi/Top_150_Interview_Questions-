class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 1; // Initialize count to track the valid elements
        for (int i = 1; i < nums.size(); i++) {
            // Check if the current element can be added
            if (count == 1 || nums[i] != nums[count - 2]) {
                nums[count] = nums[i]; // Add the element to the result
                count++;
            }
        }
        return count; // Return the number of valid elements
    }
};
