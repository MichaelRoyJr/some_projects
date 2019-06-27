package palindromechecker;

import java.util.ArrayDeque;
import java.util.Scanner;
import java.util.Stack;

public class PalindromeChecker {
  
    public static void main(String[] args) {
        // initialize data structures
        Scanner scan = new Scanner(System.in);
        String toCheck = new String();        
        Stack stack = new Stack();
        ArrayDeque queue = new ArrayDeque();
        String stackOut, queueOut = new String();
        StringBuilder temp1 = new StringBuilder();
        StringBuilder temp2 = new StringBuilder();
        
        //prompt for user input 
        System.out.println("Enter item to check: ");
        toCheck = scan.nextLine();
        
        //loop to put each character into stack and queue
        for (int i=0; i < toCheck.length(); i++) {
            stack.push(Character.toLowerCase(toCheck.charAt(i)));
            queue.add(Character.toLowerCase(toCheck.charAt(i)));
        }
        
        //empty stack        
        while (!stack.empty()) {
            temp1.append(stack.pop());
        }
        stackOut = temp1.toString();
        
        //empty the queue
        while (!queue.isEmpty()) {
            temp2.append(queue.removeFirst());
        }
        queueOut = temp2.toString();
        
        //check if palindrome
        if(queueOut.equals(stackOut)) {
            System.out.println(toCheck + " is a palindrome!");
        }
        else {
            System.out.println(toCheck + " is not a palindrome.");
        }
    }    
}
