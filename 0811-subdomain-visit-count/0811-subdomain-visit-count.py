class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # f"{count} {'.'.join(subdomain[1:])}
        ans = defaultdict(int)
        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            ans[domain] += count
            
            subdomain = domain.split('.')
            ans['.'.join(subdomain[1:])] += count
            
            if(subdomain[2:]):
                ans['.'.join(subdomain[2:])] += count
        
        return [str(c) + ' ' + d for d, c in ans.items()]