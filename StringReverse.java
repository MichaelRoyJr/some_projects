
package stringreverse;

import java.util.Scanner;

public class StringReverse {

    
    public static String reverse(String forward) {
        //convert to char array for manipulation
        char forwardChars[] = forward.toCharArray();
        char temp;
        for(int i=0; i<forward.length()/2; i++) {
            //swap first and last, second and last-1, etc 
            temp = forwardChars[i];
            forwardChars[i] = forwardChars[forward.length()-1-i];
            forwardChars[forward.length()-1-i] = temp;
            }
        //return String of modified array
        return new String(forwardChars);
    }
    public static void main(String[] args) {
        // handle input prompt and output
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String forward = scan.nextLine();
        System.out.println("Reversed: " + reverse(forward));
        
    }
    
}
