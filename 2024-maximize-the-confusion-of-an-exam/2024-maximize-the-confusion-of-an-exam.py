class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def get_ans(ch):           
            used = k
            j = 0
            ans = 0
            for i in range(len(answerKey)):
                if(answerKey[i] == ch and not used):
                    ans = max(i - j, ans)
                    while(not used and j <= i):
                        used += answerKey[j] == ch
                        j += 1

                used -= answerKey[i] == ch

            return max(ans, i - j + 1)
        
        return max(get_ans('F'), get_ans('T'))