import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] day = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++){
            if((100-progresses[i])%speeds[i] != 0){
                day[i]=(100-progresses[i])/speeds[i] + 1;
            }else{day[i]=(100-progresses[i])/speeds[i];}
        }
        List<Integer> temp = new ArrayList<>();
        int check = day[0];
        int count = 1;
        
        for (int i = 1; i < day.length; i++){
            if(check < day[i]) {
                temp.add(count);
                check = day[i];
                count = 1;
            }else{
                count ++;
            }
        } 
        temp.add(count);
        
        int[] answer = new int[temp.size()];
        for (int i = 0; i < temp.size(); i++) {
            answer[i] = temp.get(i);
        }
        
        return answer;
    }
}