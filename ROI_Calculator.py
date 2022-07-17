"""
4 boxes: Income, Expenses, Cash Flow, Cash on CASH ROI

Income:     Rental Income, Laundry, Storage, Misc.

Expenses:   tax, insurance, utilities, HOA, lawn/snow care, vacancy
            repairs, CopEx (replace), property management, mortgage

Cash Flow:  (Income - Expenses)

C on C ROI: Down payment, Closing Costs, Rehab Budget, Misc.

Calculation for Cash Return on Investment:
C on C ROI % = (Cash Flow x 12 (months)) / Total C on C ROI
"""

# Create a class that contains the 4 boxes
class Total_ROI():
    def __init__(self, income=0, expenses=0, cash_flow=0, CoC_return=0):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.CoC_return = CoC_return

    #dictionary to show the cost of each item based on user response
    def owner_income(self):
        
        your_income = {'rental income': 0,
                       'laundry income': 0,
                       'storage income': 0,
                       'misc income': 0,
                       }
        
        rent_income = input("Please enter amount for rental income, if none, type '0': ")
        if rent_income:
            your_income['rental income'] = float(rent_income)
        else: False
        
        laundry_income = input("Please enter amount for laundry income, if none, type '0': ")
        if laundry_income:
            your_income['laundry income'] = float(laundry_income)
        else: False
        
        storage_income = input("Please enter amount for storage income, if none, type '0': ")
        if storage_income:
            your_income['storage sncome'] = float(storage_income)
        else: False

        misc_income = input("Please enter total amount of any other income, if none, type '0': \n")
        if misc_income:
            your_income['misc income'] = float(misc_income)
        else: False

        self.income = sum(your_income.values())
        return f"Based on your response, your total income is: ${self.income}\n"
    
    def owner_expenses(self):

        your_expenses = {'taxes': 0,
                         'insurance': 0,
                         'water/sewer': 0,
                         'garbage': 0,
                         'electric': 0,
                         'gas': 0,
                         'HOA': 0,
                         'lawn/snow': 0,
                         'vacancy': 0,
                         'repairs': 0,
                         'CapEx': 0,
                         'prop management': 0,
                         'mortgage': 0,
                        }

        tax = input("Please enter amount for taxes, if none, type '0': ")
        if tax:
            your_expenses['taxes'] = float(tax)
        else: False

        insurance = input("Please enter amount for insurance, if none, type '0': ")
        if insurance:
            your_expenses['insurance'] = float(insurance)
        else: False

        water_sewer = input("Please enter amount for water/sewege, if none, type '0': ")
        if water_sewer:
            your_expenses['water/sewer'] = float(water_sewer)
        else: False

        garbage = input("Please enter amount for garbage, if none, type '0': ")
        if garbage:
            your_expenses['garbage'] = float(garbage)
        else: False

        electric = input("Please enter amount for electricity, if none, type '0': ")
        if electric:
            your_expenses['electric'] = float(electric)
        else: False

        gas = input("Please enter amount for gas, if none, type '0': ")
        if gas:
            your_expenses['gas'] = float(gas)
        else: False

        HOA = input("Please enter amount for HOA, if none, type '0': ")
        if HOA:
            your_expenses['HOA'] = float(HOA)
        else: False

        lawn_snow = input("Please enter amount for lawn/snow, if none, type '0': ")
        if lawn_snow:
            your_expenses['lawn/snow'] = float(lawn_snow)
        else: False

        vacancy = input("Please enter amount for vacancy, if none, type '0': ")
        if vacancy:
            your_expenses['vacancy'] = float(vacancy)
        else: False

        repairs = input("Please enter amount for repairs, if none, type '0': ")
        if repairs:
            your_expenses['repairs'] = float(repairs)
        else: False

        CapEx = input("Please enter amount for CapEX, if none, type '0': ")
        if CapEx:
            your_expenses['CapEx'] = float(CapEx)
        else: False

        prop = input("Please enter amount for property management, if none, type '0': ")
        if prop:
            your_expenses['prop management'] = float(prop)
        else: False

        mortgage = input("Please enter amount for mortgage, if none, type '0': \n")
        if mortgage:
            your_expenses['mortgage'] = float(mortgage)
        else: False

        self.expenses = sum(your_expenses.values())
        return f"Based on your response, your total expense is: ${self.expenses}\n"

    def owner_cashFlow(self):
        self.cash_flow = self.income - self.expenses
        return f"Your total annual cash flow is: ${self.cash_flow}\n"

    def CoC_returns(self):

        your_CoC_return = {'down payment': 0,
                           'closing cost': 0,
                           'rehab budget': 0,
                           'misc other': 0,}
        
        down_payment = input("Please enter amount for down payment, if none, type '0': ")
        if down_payment:
            your_CoC_return['down_payment'] = float(down_payment)
        else: False

        closing_cost = input("Please enter amount for closing cost, if none, type '0': ")
        if closing_cost:
            your_CoC_return['closing cost'] = float(closing_cost)
        else: False

        rehab_budget = input("Please enter amount for rehab budget, if none, type '0': \n")
        if rehab_budget:
            your_CoC_return['rehab budget'] = float(rehab_budget)
        else: False

        misc_other = input("Please enter total amount for anything else, if none, type '0': \n")
        if misc_other:
            your_CoC_return['misc other'] = float(misc_other)
        else: False

        self.CoC_return = sum(your_CoC_return.values())
        print(f"Based on your response, your total expense is: ${self.cash_flow} \n")

        Cash_on_Cash_return = self.cash_flow * 12 / self.CoC_return
        return f"Your total Cash on Cash Return is: {Cash_on_Cash_return}%"


def calculator():
    
    # This is to make the program run
    calc = Total_ROI()
    print(calc.owner_income())
    print(calc.owner_expenses())
    print(calc.owner_cashFlow())
    print(calc.CoC_returns())

calculator()