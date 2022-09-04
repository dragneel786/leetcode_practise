class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        def process_name(name):
            result = ""
            for c in name:
                if(c == '+'):
                    break
                    
                if(c == "."):
                    continue
                
                result += c
            
            return result
        
        
        uniq = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = process_name(local_name)
            uniq.add(local_name + '@' + domain_name)
        
        return len(uniq)
            
        