import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        char[] data = new char[s.length()];
        int check = 0;
        
        for (int i = 0; i < data.length; i++){
            data[i] = s.charAt(i);
        }
        
        for(int i = 0; i < data.length; i++){
            if(data[i] == '('){
                check ++;
            } else{
                check --;
            }
            
            if(check < 0){
                answer = false;
                break;
            }
        }
        if (check > 0) {
            answer = false;
        }

        return answer;
    }
}