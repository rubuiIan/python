class Calculator:
    def add(self, first_num, last_num):
        return first_num + last_num
    
    def subtract(self, first_num, last_num):
        return first_num - last_num
    
    def multiply(self, first_num, last_num):
        return first_num * last_num
    
    def division(self, first_num, last_num):
        return first_num / last_num
    
    def modulus(self, first_num, last_num):
        return first_num % last_num
    
    
class Inventory(Calculator):
    def __init__(self, buying_price, selling_price, units, expenses):
        super().__init__()
        self.bp = buying_price
        self.sp = selling_price
        self.units = units
        self.expenses = expenses
        
    def get_profit_or_loss(self):
        total_bought = self.multiply(self.bp, self.units)
        liabilities =  self.add(total_bought,self.expenses)
        sales_made = self.multiply(self.sp, self.units)
        result = self.subtract(sales_made, liabilities)
        if result < 0:
            return f"You made a loss of {self.multiply(result, -1)}"
        else:
            return f"You made a profit {result}"
            
inventory = Inventory(
    60000,
    65000,
    3,
    25000
)
print(inventory.get_profit_or_loss())