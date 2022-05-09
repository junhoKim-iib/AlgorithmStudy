#include<vector>
#include<iostream>
using namespace std;



class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1, mid = 0;

        while(left<right){
            mid = left + (right - left)/2;
            if(target == nums[mid]){
                return mid;
            }

            else if(target > nums[mid]){
                left = mid+1;
            }
            else right = mid;
        }
        mid = left + (right - left)/2;

        if(target> nums[mid]){
            return mid+1;
        }
        else return mid;



    }
};


int main(){
    vector<int>nums = {1,3,5,6};
    int target = 2;

    Solution S;
    int result = S.searchInsert(nums, target);

    cout<<result;
}