#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> Merge(vector<int> &A, vector<int> &B, long long &inversions) {
	/* Merge makes combines two vectors into a new vector in a sorted fashion.  indices i,j keep track of position in 
	vectors A,B respectively*/

	int j = 0;
	int i = 0;
	vector<int> C(A.size() + B.size());
	for (int k = 0; k < (A.size() + B.size()); k++) {

		//case where A and B both have entries left and value at head of B is less than value at head of A
		if (i < A.size() && j < B.size() && (A[i] > B[j])){
			C[k] = B[j];

			//each time this happens, the original array had an inverted entry
			//all entries in A should be less than entries in B, so in this case B[j] will be inverted with all 
			//remaining items in A
			inversions = (inversions + A.size() - i);
			j++;
		}

		//case where A has entries left, and value at head of B is not less than value at head of A
		else if (i < A.size()) {
			C[k] = A[i];
			i++;
		}

		//case where only B has entries left
		else {
			C[k] = B[j];
			j++;
		}
	}
	return C;
}

vector<int> MergeSort(vector<int>&inputArray, long long &inversions) {	
	/** MergeSort is a recursive algorithm to sort an array.  This function splits the vector inputArray into two new
	vectors nad recursively calls itself until size is one.  Then calls another function, Merge to recombine **/

	if (inputArray.size() > 1) {
		int newArraySize = inputArray.size() / 2;
		vector<int> A(newArraySize);
		vector<int> C(newArraySize);
		vector<int> B(newArraySize);
		vector<int> D(newArraySize);

		//adjust sizes for case of odd number vector size
		if (inputArray.size() % 2 == 1) {	
			B.resize(newArraySize + 1);
			D.resize(newArraySize + 1);

			//add last entry, which will not occur in loop below
			B[newArraySize] = inputArray[inputArray.size() - 1];
		}
		
		//populate vectors
		for (int i = 0; i < newArraySize; i++) {		
			A[i] = inputArray[i];
			B[i] = inputArray[i + newArraySize];
		}

		// make recursive call on newly created vectors
		C = MergeSort(A, inversions);
		D = MergeSort(B, inversions);

		//Merge recombines newly split arrays in a sorted fashion
		return Merge(C, D, inversions);
	}
	else {
		//base case of recursion
		return inputArray;
	}
}

int main() {
	//IntegerArray.txt contains a list of the numbers 1 - 100000 in random order
	ifstream fin("IntegerArray.txt");					
	int arraySize = 100000;

	//counter for inversions
	long long inversions = 0;					
	vector<int> sourceArray(arraySize);

	//populate vector from file
	for (int i = 0; i < arraySize; i++) {					
		fin >> sourceArray[i];
	}	

	//perform merge sort algorithm
	vector<int> outputArray(arraySize);
	outputArray = MergeSort(sourceArray, inversions);		

	cout << "Split inversions: " << inversions << endl;
	
	return 0;
}

