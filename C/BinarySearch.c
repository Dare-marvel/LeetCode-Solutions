#include<stdio.h>

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
int main()
{
int val[6] = {-1,0,3,5,9,12};
printf("%d",binarySearch(val,6,9));

return 0;
}