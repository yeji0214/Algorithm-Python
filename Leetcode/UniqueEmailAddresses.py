class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []

        for e in emails:
            local, domain = e.split('@')
            final_local = ''.join(local.split('+')[0].split('.'))

            result.append(final_local + '@' + domain)

        return len(set(result))
