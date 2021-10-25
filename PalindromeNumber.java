public class PalindromeNumber {
    public static void main(String args[]){
        PalindromeNumber s = new PalindromeNumber();
        System.out.println("Hello world");
        System.out.println(s.solution(123));
    }

    public boolean solution(int targetNumber){
        int temp = targetNumber;
        int reversedNumber = 0;
        while(temp != 0){
            int val = temp % 10;
            reversedNumber = (reversedNumber * 10) + val;
            temp /= 10;
        }

        if (reversedNumber == targetNumber)
            return true;

        return false;
    }
}
