class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        seen = set()
        for e in emails:
            s = e.split("@")
            local, domain = "".join(s[0].split("+")[0].split(".")), s[1]
            if (local, domain) not in seen:
                seen.add((local, domain))
                res += 1
        return res
