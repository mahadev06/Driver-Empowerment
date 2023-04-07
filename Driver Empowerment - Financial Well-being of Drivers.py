# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:01:46 2023

@author: Mahadev Mondal
"""

import random

# Define function to calculate income and expenses
def calculate_income_expenses():
    income = random.randint(2000, 10000)
    expenses = random.randint(1500, 8000)
    return income, expenses

# Budgeting algorithm to prioritize expenses
def prioritize_expenses(income, expenses):
    budget = {'Housing': 0.3 * income, 'Transportation': 0.15 * income,
              'Food': 0.1 * income, 'Utilities': 0.1 * income,
              'Debt payments': 0.2 * income, 'Savings': 0.15 * income}
    remaining_income = income - expenses
    for category in budget:
        if remaining_income <= 0:
            break
        if remaining_income < budget[category]:
            budget[category] = remaining_income
            break
        budget[category] = budget[category]
        remaining_income -= budget[category]
    return budget

# Implement a savings plan
def calculate_savings(income, savings_percent):
    savings_amount = income * savings_percent / 100
    return savings_amount

# Investment algorithm to guide drivers
def investment_algorithm(savings_amount):
    investment_options = ['Stocks', 'Bonds', 'Real Estate']
    recommended_investment = random.choice(investment_options)
    return recommended_investment

# Incentive program to reward saving and investing
def incentive_program(savings_amount, investment_made):
    reward_points = savings_amount // 1000
    if investment_made == 'Stocks':
        reward_points += 100
    elif investment_made == 'Bonds':
        reward_points += 50
    else:
        reward_points += 20
    return reward_points

# Automatic savings program
def automatic_savings_program(income, savings_percent):
    savings_account = 0
    savings_amount = calculate_savings(income, savings_percent)
    savings_account += savings_amount
    return savings_account

# Investment algorithm that considers investment goals and risk tolerance
def investment_algorithm_2(investment_goal, risk_tolerance):
    investment_options = {'High Risk': ['Stocks', 'Real Estate'],
                          'Medium Risk': ['Bonds', 'Mutual Funds'],
                          'Low Risk': ['Savings Account', 'CD']}
    recommended_investment = random.choice(investment_options[risk_tolerance])
    return recommended_investment

# Loan approval algorithm that considers credit history and financial track record
def loan_approval_algorithm(credit_score, income):
    loan_approval = False
    if credit_score >= 700 and income >= 3000:
        loan_approval = True
    return loan_approval

# Loan repayment algorithm with more flexible repayment terms
def loan_repayment_algorithm(amount_borrowed, interest_rate, loan_term):
    monthly_payment = (amount_borrowed * interest_rate / 100) / (12 * (1 - (1 + (interest_rate / 100) / 12) ** (-loan_term)))
    return monthly_payment

# Retirement planning algorithm
def retirement_planning_algorithm(age, current_income, retirement_income_percent):
    retirement_income = retirement_income_percent / 100 * current_income
    years_to_retirement = 65 - age
    required_savings = retirement_income * 12 * years_to_retirement
    monthly_savings = required_savings / (years_to_retirement * 12)
    return monthly_savings

# Example usage
income, expenses = calculate_income_expenses()
print("Income:", income)
print("Expenses:", expenses)
budget = prioritize_expenses(income, expenses)

savings_percent = 10
savings_amount = calculate_savings(income, savings_percent)
print("Savings amount:", savings_amount)

recommended_investment = investment_algorithm(savings_amount)
print("Recommended investment:", recommended_investment)

reward_points = incentive_program(savings_amount, recommended_investment)
print("Reward points:", reward_points)

savings_account = automatic_savings_program(income, savings_percent)
print("Savings account balance:", savings_account)

investment_goal = 'Retirement'
risk_tolerance = 'Medium Risk'
recommended_investment = investment_algorithm_2(investment_goal, risk_tolerance)
print("Recommended investment:", recommended_investment)

credit_score = 750
loan_approval = loan_approval_algorithm(credit_score, income)
print("Loan approval:", loan_approval)

amount_borrowed = 10000
interest_rate = 10
loan_term = 24
monthly_payment = loan_repayment_algorithm(amount_borrowed, interest_rate, loan_term)
print("Monthly loan repayment:", monthly_payment)

age = 30
current_income = 50000
retirement_income_percent = 70
monthly_savings = retirement_planning_algorithm(age, current_income, retirement_income_percent)
print("Monthly savings for retirement:", monthly_savings)