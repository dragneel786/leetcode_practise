class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        dp = [([None] * 3) for _ in range(3)]
        counts = {"X":0, "O":0}
        wins = {"X":False, "O":False}
        for i in range(3):
            for j in range(3):
                if(board[i][j] == " "):
                    continue
                
                p = board[i][j]
                counts[p] += 1
                dp[i][j] = defaultdict(lambda:defaultdict(lambda:0))
                dp[i][j][p]["u"], dp[i][j][p]["l"],\
                dp[i][j][p]["d"], dp[i][j][p]["a"] = 1, 1, 1, 1
                if(i > 0 and dp[i - 1][j]):
                    dp[i][j][p]["u"] += dp[i - 1][j][p]["u"]
                
                if(j > 0 and dp[i][j - 1]):
                    dp[i][j][p]["l"] += dp[i][j - 1][p]["l"]
                    
                if(i > 0 and j > 0 and dp[i - 1][j - 1]):
                    dp[i][j][p]["d"] += dp[i - 1][j - 1][p]["d"]
                
                if(i > 0 and j < 2 and dp[i - 1][j + 1]):
                    dp[i][j][p]["a"] += dp[i - 1][j + 1][p]["a"]
                    
                if(3 in [dp[i][j][p]["d"], dp[i][j][p]["u"],\
                         dp[i][j][p]["l"], dp[i][j][p]["a"]]):
                    wins[p] = True
        
        diff = counts["X"] - counts["O"]
        if(diff not in [0, 1] or all(wins.values())):
            return False
        
        if((wins['X'] and diff != 1) or (wins["O"] and diff != 0)):
            return False
    
        return True