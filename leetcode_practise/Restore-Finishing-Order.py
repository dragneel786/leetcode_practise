class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        iorder = {v: i for i, v in enumerate(order)}
        friends.sort(key=lambda x: iorder[x])
        return friends
