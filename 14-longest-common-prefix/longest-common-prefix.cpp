class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        for(int i=0;i<strs[0].length();i++)
        {
            char start=strs[0][i];
            for(int j=0;j<strs.size();j++)
            {
                if(start!=strs[j][i])
                return ans;
            }
            ans+=start;
        }
        return ans;
    }
};