import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParanthesis {
    public static void main(String args[]){
        ValidParanthesis vp = new ValidParanthesis();
        System.out.println(vp.isValid("([)]"));
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            if(curr == '(' || curr == '{' || curr == '['){
                stack.push(curr);
                continue;
            }

            if(stack.empty())
                return false;

            char stackLastChar = stack.pop();
            
            if(stackLastChar == '(' && curr != ')')
                return false;

            if(stackLastChar == '{' && curr != '}')
                return false;
            
            if(stackLastChar == '[' && curr != ']')
                return false;
        }

        if(!stack.empty())
            return false;

        return true;
    }
   
}
