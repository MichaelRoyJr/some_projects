Description
  This finds the minimum cut of a connected graph using Karger's Random contraction
  Algorithm. This algorithm uses random contraction of edges in the graph.  Each pass
  picks an edge, and compresses its end vertices into a single vertex.  Edges from
  each original vertex are merged into the single new vertex and self loops are removed.
  Though each pass yields a low (~1/n^2) success rate, it is nonzero. Multiple passes
  are required to ensure statistically, the actual value will be achieved.  In this
  case the minimum repetitions required is n^2 * log(n).

  This repository will feature the evolution of this design from the quite naive,
  to hopefully, a quite optimized implementation.  Rough measurements of run time
  using a standardized number of passes have been recorded with a stopwatch.
  Original run time of full length (211600 passes) took over seven hours -- Not Good!
  Updates will continue. 

  Current Version:
    Very rough.  First version that achieved correctness. No optimizations done yet.

  Run Time (2000 passes):
    3:26


Highlights
    -Algorithm design
    -Adjacency list graph representation
    -Randomization
    -Optimization

To Run
  This was written in C# using Visual Studio 2017.  Included are the .cs file as
  well as the .txt document with the array that is hard coded into the project.
  If using Visual Studio, copy the text file into your projects bin/Debug folder.
  Otherwise use your favorite C# compiler.

  At the present, the number of repetitions is limited to 2000 as a baseline for
  measurement.  To run the actual program use the value in the comments
