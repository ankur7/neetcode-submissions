class Solution:
    def __init__(self):
        self.delimiter = "&!@#$%"

    def encode(self, strs: List[str]) -> str:
        pre_delimit_str = ''
        post_delimit_str = ''
        
        for word in strs:
            word_len = len(word)
            pre_delimit_str += '#' + str(word_len)
            post_delimit_str += word

        # ["Hello","World"]
        # '5#5' + self.delimiter + 'HelloWorld'

        return pre_delimit_str + self.delimiter + post_delimit_str


    def decode(self, s: str) -> List[str]:
        # print('s', s)
        pre_delimit_str, post_delimit_str = s.split(self.delimiter)

        word_lengths = pre_delimit_str.split('#')
        word_lengths = [int(wlen) for wlen in word_lengths if wlen]
        # print('word_lengths', word_lengths)
        result = []
        offset = 0

        for w_len in word_lengths:
            cur_word = post_delimit_str[offset: offset + w_len]
            result.append(cur_word)
            offset = offset + w_len

        return result
        