class Category:
    def __init__(self, category):
        self.category = category
        self.balance = 0.0
        self.ledger = list()

    def check_funds(self, amount):
        return amount <= self.balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount, description=""):
        self.balance = self.balance + amount
        self.ledger.append({"amount": amount, "description": description})        
        
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance = self.balance - amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            category.deposit(amount, "Transfer from " + self.category )
            self.withdraw(amount, "Transfer to " + category.category)
            return True
        else:
            return False

    def __str__(self):
        total = 0
        s = "*" * int( (30-len(self.category)) / 2)
        s += self.category
        s = s.ljust(30,"*") + "\n"
        for item in self.ledger:
            s += item["description"][:23].ljust(23)
            s += "{:.2f}".format(item["amount"]).rjust(7)
            total += item["amount"]
            s += "\n"
        s += "Total: " + "{:.2f}".format(total)
        return s
        
def create_spend_chart(categories):
    amounts = []
    names = []
    total = 0.0
    for i in range(len(categories)):
        names.append(categories[i].category)
        amounts.append(0)
        for item in categories[i].ledger:  
            if(item["amount"] < 0):          
                amounts[i] -= item["amount"]        
        total += amounts[i]
    for i in range(len(amounts)):
        amounts[i] = 100.0 * amounts[i] / total 
        amounts[i] = round(amounts[i] - (amounts[i] % 10), -1)
    s="Percentage spent by category\n"
    for i in range(100,-10,-10):
        s += str(i).rjust(3) + "| "
        for j in range(len(amounts)):
            if(i <= amounts[j]):
                s+= "o  "
            else:
                s+= "   "
        s += "\n"
    s += "    -" + ("---"*len(amounts)) + "\n"
    maxlen = 0
    for i in names:
        maxlen = max(maxlen, len(i))            
    for i in range(maxlen):
        s2 = "     "
        for j in names:
            if(i < len(j)):
                s2 += j[i] + "  "
            else:
                s2 += "   "        
        s += s2 
        if(i < maxlen-1):
            s += "\n"
    return s
