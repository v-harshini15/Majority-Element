Given an array of size n, find the majority element. The majority element is the element that
appears more than floor(n/2) times.
You may assume that the array is non-empty, and the majority element always exist in the array.
Example:
Input : [2, 1, 2]
Return : 2 which occurs 2 times which is greater than 3/2.


nitialization:

Initialize candidate to the first element of the array (nums[0]) and set count to 1.
Voting Process:

Iterate through the array starting from the second element.
If count becomes 0, update the candidate to the current element and reset count to 1.
If the current element is the same as the candidate, increment count; otherwise, decrement count.
Verification:

After the first iteration, the candidate holds the potential majority element.
To verify, iterate through the array again and count the occurrences of the candidate.
Result:

Return the candidate as the majority element.
Example:

The provided example input array [2, 1, 2] is used to demonstrate the algorithm.
The algorithm identifies 2 as the majority element as it occurs more than 3/2 times in the array.
