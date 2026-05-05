class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = len(students)
        studentCount = defaultdict(int)
        for s in students:
            studentCount[s] +=1
        for sand in sandwiches:
            if studentCount[sand] > 0:
                studentCount[sand] -=1
                count -=1
            else:
                return count
        return count
            
            
            
            


