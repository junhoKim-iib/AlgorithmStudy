#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;



class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        vector<int>result;   
        for(int i = 0; i<nums.size();i++){
            result.push_back(nums[i]*nums[i]);
        }

        return result;
    }
};

int main(){
    vector<int>nums = {-4,-1,0,3,10};


    Solution S;
    
    vector<int>result = S.sortedSquares(nums);
    sort(result.begin(),result.end());
    cout<<'[';

    for(int i = 0; i<result.size() -1;i++){
        cout << result[i] << ',';
    }
    
    cout<< result[result.size()-1] <<']';

}