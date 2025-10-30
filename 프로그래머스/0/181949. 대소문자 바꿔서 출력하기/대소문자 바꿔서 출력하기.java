import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";
        
        for (int i = 0; i < a.length(); i++) {
            char chr = a.charAt(i);
            
            if (Character.isUpperCase(chr)) {
                result += Character.toLowerCase(chr);
            }
            else{
                result += Character.toUpperCase(chr);
            }
        }
        System.out.println(result);
    }
}