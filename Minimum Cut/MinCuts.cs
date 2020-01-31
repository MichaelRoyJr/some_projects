using System;
using System.IO;
using System.Collections;

namespace AlgorithmsAssignment3WithLists
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList[] A = new ArrayList[201];
            string inString;
            int edge1,
                edge2,
                n = 200,
                t = 0;
            Random generate = new Random();
            ArrayList results = new ArrayList();

            //for measurement
            Console.WriteLine("press any key to begin");
            Console.ReadKey();

            //repeat until it works
            while (t < 2000) {
            //211600 for viable result

                //retrieve input from file
                try
                {
                    StreamReader inFile = new StreamReader("kargerMinCut.txt");
                    int i = 1;
                    while ((inString = inFile.ReadLine()) != null)
                    {
                        string[] tempString = inString.Split(new char[] { '\t' }, StringSplitOptions.RemoveEmptyEntries);
                        A[i] = new ArrayList();
                        foreach (string item in tempString)
                        {
                            A[i].Add(int.Parse(item));
                        }
                        i++;
                    }
                }
                catch (System.IO.IOException exc)
                {
                    Console.WriteLine("Error!!!");
                    Console.WriteLine(exc.Message);
                }

                n = 200;
                while (n > 2)
                {
                    //randomly pick edge to contract
                    edge1 = generate.Next(1, 201);
                    while (A[edge1].Count == 0)
                        edge1 = generate.Next(1, 201);
                    edge2 = generate.Next(1, 201);
                    while (!A[edge1].Contains(edge2) || edge1 == edge2)
                        edge2 = generate.Next(1, 201);

                    //remove self-loops
                    while (A[edge1].Contains(edge2))
                        A[edge1].Remove(edge2);
                    //combine edges
                    foreach (int entry in A[edge2])
                    {
                        if (entry != edge1 && entry != edge2)
                        {
                            A[edge1].Add(entry);
                            while (A[entry].Contains(edge2))
                            {
                                A[entry].Add(edge1);
                                A[entry].Remove(edge2);
                            }
                        }
                    }
                    //mark as done
                    A[edge2].Clear();

                    n--;
                    if (n == 2)
                    {
                        results.Add(A[edge1].Count - 1);
                    }
                }
                t++;
                if (t % 100 == 0)
                    {
                        Console.Clear();
                        Console.WriteLine(t);
                    }
            }
            int winner = 20;
            foreach(int min in results)
            {
                if (min < winner)
                    winner = min;
            }
            Console.WriteLine("Winner is: " + winner);

            /** view array for debugging -- use on single pass
             * for (int i = 1; i < 201; i++)
            {
                foreach (int entry in A[i])
                {
                    Console.Write(entry + " ");
                }
                Console.WriteLine();
            } **/
        }
    }
}
