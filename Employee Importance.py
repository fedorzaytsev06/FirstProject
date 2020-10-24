"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # print(employees[0])
        # print(employees[1])
        # print(employees[2])
        print(id)
        worker = []
        for i in range(len(employees)):
            if employees[i][0] == id:
                worker = employees[i]
                break
        print(worker, worker[2])



s = Solution()
s.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)