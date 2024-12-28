class Solution {
public:
    int search(vector<int>& nums, int target) {
        vector<pair<int,int>>v(nums.size());
        for(int i=0;i<nums.size();i++)
        {
            v[i].first=nums[i];
            v[i].second=i;
        }
        sort(v.begin(),v.end());
        int l=0,r=nums.size()-1,mid=0;
        while(l<=r)
        {
            mid=(l+r)/2;
            if(v[mid].first==target)
                return v[mid].second;
            else if(v[mid].first<target)
            {
                l=mid+1;
            }
            else r=mid-1;
        }
        return -1;
    }
};