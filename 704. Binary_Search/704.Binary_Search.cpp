
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int pivot, left = 0, right = nums.size() -1;
        while(left <= right){
            //(left + right) / 2 실패 참고  https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
            pivot = ((unsigned int)left + (unsigned int)right) >> 1; // 
            if(nums[pivot] == target){
                return pivot;
            }
            
            else if(nums[pivot]< target){
                left = pivot + 1; 
            }
            else right = pivot -1;
        }
        return -1;
    }
};