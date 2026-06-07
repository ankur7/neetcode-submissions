class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            min_len = min(len(w1), len(w2))
            mismatch_found = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    mismatch_found = True
                    break

            # all characters matched for the shorter word
            if not mismatch_found and len(w1) > len(w2):
                return False

        return True
