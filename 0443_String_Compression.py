class Solution:
    def compress(self, chars: List[str]) -> int:
        length = 0

        last_seen = chars[0]
        n = 1

        chars.append("end")
        for i in range(1, len(chars)):
            if chars[i] == last_seen:
                n += 1
            else:
                chars[length] = last_seen
                if n > 1:
                    n = str(n)
                    for n_i in range(len(n)):
                        chars[length + 1 + n_i] = n[n_i]
                    length += len(n)
                length += 1
                last_seen = chars[i]
                n = 1

        return length
