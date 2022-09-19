class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        contentToListMap = defaultdict(list)
        for path in paths:
            splited_files = path.split(' ')
            
            for file in splited_files[1:]:
                file, content = file.split("(")
                
                contentToListMap[content]\
                .append(splited_files[0] + "/" + file)
            
        return [value for value in contentToListMap\
                .values() if(len(value) >= 2)]
                
        
        
        