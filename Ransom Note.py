class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_ch = list(ransomNote)
        m_ch = list(magazine)

        for char in r_ch:
            if char in m_ch:
                m_ch.remove(char)
            else:
                return False
        return True