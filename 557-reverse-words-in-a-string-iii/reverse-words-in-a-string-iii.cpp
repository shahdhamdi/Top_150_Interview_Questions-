class Solution {
public:
    string reverseWords(string s) {
        int n=s.size();
        string reversed="";
        string ans="";
        for(int i=0;i<n;i++)
        {
            if(s[i]==' '||i==n-1)
            {
                if(i==n-1)
                {
                    reversed+=s[i];
                }
                reverse(reversed.begin(),reversed.end());
                ans+=reversed;
                if(i!=n-1)
                {
                    ans+=' ';
                }
                reversed="";
            }
            else
            {
                reversed+=s[i];
            }
            }
       
        return ans;
    }
};