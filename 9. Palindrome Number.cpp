class Solution {
public:
    bool isPalindrome(int x) {
        int a[20];
        int i =0;
        if(x<0){
            return false;
        }
        while(x){
            int b=x%10;
            a[i]=b;
            i++;
            x=x/10;
        }
        for(int k=0,j=i-1;j>=k;k++,j--){
            if(a[k]!=a[j]){
                return false;
            }
        }
        return true;
    }
};
