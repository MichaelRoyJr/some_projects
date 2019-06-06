package wordcounter;

import java.io.File;
import java.util.Scanner;

public class WordCounter {

    public static void main(String[] args) throws Exception{
        //Prompt for filename
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the name of the file: ");
        String filename = scan.nextLine();
        //Use new scanner to read from file
        File file = new File(filename);
        Scanner scan2 = new Scanner(file);
        int wordCount = 0;
        while(scan2.hasNext()) {
            //count words and advance scanner
            wordCount++;
            scan2.next();
        }
        System.out.println("The word count of file: \"" + filename + "\" is: " + wordCount);
    }
    
}
