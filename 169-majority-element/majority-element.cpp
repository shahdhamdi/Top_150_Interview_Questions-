class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        int majority_element;
        unordered_map<int, int> freq;
        for(int i=0;i<n;i++)
        {
            freq[nums[i]]++;
        }
        for(int i=0;i<n;i++)
        {
            if(freq[nums[i]]>n/2)
            {
                majority_element=nums[i];
                break;
            }
        }
        return majority_element;
    }
};
