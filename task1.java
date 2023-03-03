import java.util.Scanner;

public class ReverseSubstring {
    public static void main(String[] args) {
      
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a paragraph: ");
        String paragraph = scanner.nextLine();

 
        String reversedParagraph = reverseSubstring(paragraph);

        System.out.println(reversedParagraph);
    }

    public static String reverseSubstring(String s) {
        if (s.length() <= 1) {
            return s;
        } else {
            int mid = s.length() / 2;
            String left = s.substring(0, mid);
            String right = s.substring(mid);
           
            Thread leftThread = new Thread(() -> {
                reverseSubstring(left);
            });
            Thread rightThread = new Thread(() -> {
                reverseSubstring(right);
            });
            leftThread.start();
            rightThread.start();
            try {
                
                leftThread.join();
                rightThread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
           
            return new StringBuilder(right).reverse().toString() +
                   new
