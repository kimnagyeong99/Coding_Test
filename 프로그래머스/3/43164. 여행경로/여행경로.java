import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        int n = tickets.length;
        
        Arrays.sort(tickets, (a,b) -> {
            if(!a[0].equals(b[0])) return a[0].compareTo(b[0]);
            return a[1].compareTo(b[1]);
        });
        
        boolean[] used = new boolean[n];
        List<String> path = new ArrayList<>();
        
        path.add("ICN");
        
        dfs("ICN", tickets, used, path, 0);
        
        return path.toArray(new String[0]);
    }
    public boolean dfs(String cur, String[][] tickets, boolean[] used, List<String> path, int usecount){
        if(usecount == tickets.length){
            return true;
        }
        
        for(int i = 0; i < tickets.length; i++){
            if(tickets[i][0].equals(cur) && !used[i]){
                used[i] = true;
                path.add(tickets[i][1]);
                
                if(dfs(tickets[i][1], tickets, used, path, usecount+1)){
                    return true;
                }
                
                used[i] = false;
                path.remove(path.size() - 1);
            }
        }
        return false;
    }
}