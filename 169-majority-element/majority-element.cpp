class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int majority_element;
        unordered_map<int, int> freq;
        
        // Count frequency of each element
        for (int i = 0; i < n; i++) {
            freq[nums[i]]++;
        }
        
        // Find the element with frequency greater than n/2
        for (int i = 0; i < n; i++) {
            if (freq[nums[i]] > n / 2) {
                majority_element = nums[i];
                break;
            }
        }
        
        return majority_element;
    }
};
