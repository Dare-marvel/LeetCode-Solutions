//Link to the problem : https://leetcode.com/problems/binary-search/

int binarySearch(int nums[], int n, int key) {
    int st = 0, end = n - 1, mid = (st + end) / 2;
    while (st <= end) {
        if (nums[mid] == key) {
            return mid;
        }
        else if (nums[mid] > key) {
            end = mid - 1;
        }
        else {
            st = mid + 1;
        }
        mid = (st + end) / 2;
    }
    return -1;
}
