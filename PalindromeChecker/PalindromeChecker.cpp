#include <iostream>
#include <string>
#include <stack>
#include <queue>
using namespace std;

int main() {
	//initialize data structures
	stack<char> charStack;
	queue<char> charQueue;
	string toCheck, stackOut, queueOut;
	string temp;

	//accept item to check
	cout << "Enter item to check: ";
	getline(cin, toCheck);	
	
	//populate stack and queue
	for (int i = 0; i < toCheck.size(); i++) {
		charStack.push(tolower(toCheck[i]));
		charQueue.push(tolower(toCheck[i]));
	}

	//empty the stack
	while (!charStack.empty()) {
		stackOut += charStack.top();
		charStack.pop();
	}

	//empty the queue
	while (!charQueue.empty()) {
		queueOut += charQueue.front();
		charQueue.pop();
	}

	//check if palindrome
	if (queueOut == stackOut)
		cout << endl << toCheck << " is a palindrome!";
	else
		cout << endl << toCheck << " is not a palindrome.";

    return 0;
}

