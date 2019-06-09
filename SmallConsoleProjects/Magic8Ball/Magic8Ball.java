package magic8ball;

import java.util.Random;
import java.util.Scanner;


public class Magic8Ball {
      
    public static void main(String[] args) {
        //create string array with possible responses
        String responses[] = {"It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"};
           
        boolean play = true;
        Scanner scan = new Scanner(System.in);
        while(play==true) {
            System.out.println("Welcome to the Magic 8 Ball. Please ask a yes or no question: ");
            String question = scan.nextLine();
            //get random number 0-19 to index responses[]
            Random rand = new Random();
            int index = rand.nextInt(20);
            String response = responses[index];
            //display answer
            System.out.println("The answer to your question, " + question + " is: " + response);
            System.out.println("Would you like to play again: ");
            String answer = scan.nextLine();
            //exit loop when user done
            if(answer.equalsIgnoreCase("NO")||answer.equalsIgnoreCase("n")) {
                play = false;
            }           
        }
                
    }
    
}
