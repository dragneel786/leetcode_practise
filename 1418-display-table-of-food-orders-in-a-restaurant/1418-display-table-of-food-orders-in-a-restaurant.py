class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        tmap = defaultdict(list)
        unique_dishes = set()
        for name, table, dish in orders:
            tmap[table].append(dish)
            unique_dishes.add(dish)
        
        row1 = ["Table"] + sorted(unique_dishes)
        res = [row1]
        for table_no in sorted(tmap.keys(), key=lambda x:int(x)):
            new_row = [table_no]
            for row_name in row1[1:]:
                new_row.append(
                    str(tmap[table_no].count(row_name))
                )
            
            res.append(new_row)
        
        return res
            
        