/** This counts the number of inversions (numbers out of order) in a large array using a version of a merge-sort algorithm.
    As the sorted arrays are merged after all recursions are done each item skipped in 'left-hand' array is an inverion.
**/

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> Merge(vector<int> &A, vector<int> &B, long long &inversions) {
	int j = 0;
	int i = 0;
	vector<int> C(A.size() + B.size());
	for (int k = 0; k < (A.size() + B.size()); k++) {
		if (i < A.size() && j < B.size() && (A[i] > B[j])){
			C[k] = B[j];
			inversions = (inversions + A.size() - i);
			j++;
		}
		else if (i < A.size()) {
			C[k] = A[i];
			i++;
		}
		else {
			C[k] = B[j];
			j++;
		}
	}
	return C;
}

vector<int> MergeSort(vector<int>&inputArray, long long &inversions) {	
	if (inputArray.size() > 1) {
		int newArraySize = inputArray.size() / 2;
		vector<int> A(newArraySize);
		vector<int> C(newArraySize);
		vector<int> B(newArraySize);
		vector<int> D(newArraySize);
		if (inputArray.size() % 2 == 1) {
			B.resize(newArraySize + 1);
			D.resize(newArraySize + 1);
		}
		
		for (int i = 0; i < newArraySize; i++) {
			A[i] = inputArray[i];
			B[i] = inputArray[i + newArraySize];
		}
		if (inputArray.size() % 2 == 1) {
			B[newArraySize] = inputArray[inputArray.size() - 1];
		}
		C = MergeSort(A, inversions);
		D = MergeSort(B, inversions);

		return Merge(C, D, inversions);
	}
	else {
		return inputArray;
	}
}

int main() {

	ifstream fin("IntegerArray.txt");
	int arraySize = 100000;
	long long inversions = 0;
	vector<int> sourceArray(arraySize);
	for (int i = 0; i < arraySize; i++) {
		fin >> sourceArray[i];
	}	

	vector<int> outputArray(arraySize);
	outputArray = MergeSort(sourceArray, inversions);

	for (int j = 0; j < 1000; j++) {
		cout << outputArray[j] << endl;
	}

	cout << "Split inversions: " << inversions << endl;
	
	return 0;
}

