Description
  This program implements the Quick Sort algorithm to sort an array populated
  with arbitrary values.  The algorithm works by selecting an element to be the
  pivot, and then sorting the items into two partitions, one with all values
  less than the pivot, one with values all greater.  These for now are unordered.
  Each partition is processed recursively until the whole array is sorted.  Each
  pass runs in linear time, and on average the whole algorithm is in O(n log n).

Highlights
  -Recursive algorithm design
  -Randomization technique
  -Optimization with pivot selection
  -Asymptotic analysis

To run
  This was written in C# using Visual Studio 2017.  Included are the .cs file as
  well as the .txt document with the array that is hard coded into the project.
  If using Visual Studio, copy the text file into your projects bin/Debug folder.
  Otherwise use your favorite C# compiler.    
