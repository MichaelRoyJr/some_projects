Description
    CountInversions.cpp uses a merge sort algorithm to count the number of inversions, i.e. the 
    number of out of order entries in a large array.  It works by recursively splitting the array 
    in half until it is of size one, then 'merging' the split halves together in sorted order.  As
    the array is being reconstructed, if the first entry in the second-half array is smaller than 
    the first entry in the first half array, an entry in the original was inverted.  This was 
    originally conceived to solve a particular problem, so the included file is directly 
    referenced in the code.

Highlights
    -Algorithm design
    -Recursion
    -Container classes

To Run 
    Make sure IntegerArray.txt is in same directory as CountInversions.cpp.  Build and execute in 
    your preferred c++ compiler/ IDE.  I used Visual Studio 2017.

