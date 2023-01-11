import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RomanNumbers {
    public static void main(String args[]){
        RomanNumbers r = new RomanNumbers();
        System.out.println(r.romanToInt("MCMXCIV"));
    }
    public int romanToInt(String s) {
        Map<Character, ArrayList<Integer>> hmap = new HashMap<>();
        hmap.put('I', new ArrayList<Integer>(Arrays.asList(0, 1)));
        hmap.put('V', new ArrayList<Integer>(Arrays.asList(1, 5)));
        hmap.put('X', new ArrayList<Integer>(Arrays.asList(2, 10)));
        hmap.put('L', new ArrayList<Integer>(Arrays.asList(3, 50)));
        hmap.put('C', new ArrayList<Integer>(Arrays.asList(4, 100)));
        hmap.put('D', new ArrayList<Integer>(Arrays.asList(5, 500)));
        hmap.put('M', new ArrayList<Integer>(Arrays.asList(6, 1000)));

        int number = 0;
        boolean add = false;
        for(int i = 0; i < s.length(); i++){
            System.out.println(add);
            ArrayList<Integer> curr_arr =  hmap.get(s.charAt(i));
            ArrayList<Integer> ahead_arr = new ArrayList<>();
            if(i != (s.length() - 1)){
                ahead_arr =  hmap.get(s.charAt(i + 1));
            }

            if (add){
                number += (curr_arr.get(1) - hmap.get(s.charAt(i - 1)).get(1));
                add = false;
            }
            else {
                if(i == (s.length() - 1) || curr_arr.get(0) >= ahead_arr.get(0)){
                    number += curr_arr.get(1);
                    add = false;
                }
                else{
                    add = true;
                }
            }
            // System.out.println(number);
        }
        return number;
    }
}

/*
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/