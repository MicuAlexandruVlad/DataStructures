# Active Directory

Uses recursion to find a certain user in a tree of groups. Has a space complexity of O(n). In the worst case scenario the user is not found, hence all the `Group` objects need to be visited. If all n groups have m subgroups then the time complexity is O(m*n)
