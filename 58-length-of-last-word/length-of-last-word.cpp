class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans=0;
        bool check=0; 
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]!=' ')
            {
                ans++;
                check=1;
            }
            else if(s[i]==' '&&check)
            {
               break;
            }
        }
        return ans;
    }
};