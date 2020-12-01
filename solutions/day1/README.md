**Task**: Find a sum of two integers in a set of n integers that, when added, equal to 2020. Then, display their product.

*First idea* 
First we can consider a brute-force approach of generating all possible pairs of numbers and calculating each one. This will not be efficient for large sets, we can do better than this!

*What if we sort the set?*
When the set is sorted we get a better approximation of possible combinations. We can look at the largest number and see how far from our target we are. 

We start looking at two opposite sides of the array. If the sum of the first and last element is > 2020, we reject the last element and compare the first element to last - 1. If it's < 2020, we look at the second element of the array.

