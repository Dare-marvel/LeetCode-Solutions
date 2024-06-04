### [Assign Cookies](https://leetcode.com/problems/assign-cookies/description/)

## Explanation:
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

The approach taken in the provided code is as follows:

1. Sort the greed factors of the children (g) and the sizes of the cookies (s) in ascending order.
   - Sorting ensures that we can efficiently match the smallest greed factors with the smallest cookie sizes.

2. Initialize two pointers, `l` and `r`, to iterate over the sorted cookie sizes and greed factors, respectively.

3. Iterate through the sorted cookie sizes and greed factors using the two pointers.
   - For each iteration, check if the current cookie size (s[l]) is greater than or equal to the current greed factor (g[r]).
     - If it is, increment the `r` pointer, indicating that the current child is content and can be assigned the cookie.
   - Increment the `l` pointer to move to the next cookie size.

4. After the iteration, the value of `r` represents the number of content children (or assigned cookies).

5. Return the value of `r` as the maximum number of content children.

The intuition behind this approach is as follows:

- By sorting both the greed factors and cookie sizes, we ensure that the smallest greed factors are matched with the smallest cookie sizes first.
- This greedy approach maximizes the number of content children because it assigns the smallest available cookies to the children with the smallest greed factors, ensuring that the largest number of children are satisfied.
- The iteration continues until either all children are assigned cookies or all cookies are exhausted.
- The final value of `r` represents the number of children who were successfully assigned cookies that satisfy their greed factors.

The provided code offers an efficient solution to the "Assign Cookies" problem by leveraging sorting and a greedy approach. The sorting step ensures that the smallest greed factors are matched with the smallest cookie sizes, maximizing the number of content children. The time complexity is dominated by the sorting operations, while the space complexity remains constant.
## Time and Space Complexity:
### `Time Complexity`:
- The time complexity of the solution is O(n log n + m log m), where n is the size of the greed factor vector (g), and m is the size of the cookie size vector (s).
- This complexity arises from the sorting operations performed on both vectors, which typically have a time complexity of O(n log n) for common sorting algorithms like quicksort or merge sort.
- The iteration over the sorted vectors takes O(n + m) time, which is bounded by the sorting time complexity.

### `Space Complexity`:
- The space complexity of the solution is O(1), as it does not use any additional data structures that scale with the input size.
- The sorting operations are performed in-place, modifying the original input vectors.

## Code:
```cpp
class Solution {
public:
    // Function to find maximum number of children who can have content
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Size of the two vectors
        int n = g.size() , m = s.size();

        // Two pointers initialized to the start of g[] and s[]
        int l = 0, r = 0;

        // Sorting the 'g' vector (children) and 's' vector (cookies)
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());

        // Loop until we reach the end of either 'g' or 's'
        while(l < m && r < n){
            // If size of the cookie s[l] is greater than or equal to g[r]
            // then this cookie can be given to the child
            if(g[r] <= s[l]){
                r += 1; // Move to the next child
            }
            l += 1; // Move to the next cookie
        }

        // Return the maximum number of children who can have content
        return r;
    }
};

```
