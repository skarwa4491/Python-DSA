import sys
class Solution():
    max = sys.maxsize *-1
    def findMax(self, items , cost, bag_weight , item_cost ,current_weight, idx):
        if current_weight > bag_weight:
            return 0
        if idx==len(items) or current_weight==bag_weight:
            if current_weight<=bag_weight and item_cost >=self.max:
                self.max=item_cost
            return

        self.findMax(items,cost,bag_weight,item_cost+cost[idx],current_weight+items[idx],idx+1)
        self.findMax(items,cost,bag_weight,item_cost,current_weight,idx+1) 


max = Solution()
max.findMax(items=[2,5,1,3,4],cost=[15,14,10,45,30],bag_weight=7,item_cost=0,current_weight=0,idx=0)
print(max.max)
