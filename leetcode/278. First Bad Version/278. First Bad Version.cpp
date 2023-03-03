// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left < right){
            int pivot = left + (right - left) / 2;
            if(isBadVersion(pivot))
                right = pivot;
            else left = pivot + 1;
        }
    return left;
    }
};