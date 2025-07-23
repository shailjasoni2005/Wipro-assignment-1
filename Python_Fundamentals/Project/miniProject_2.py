'''
Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
'''

hourly_cost = 0.51

cost_per_day = hourly_cost * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

print("Cost to operate one server per day: $", cost_per_day)
print("Cost to operate one server per week: $", cost_per_week)
print("Cost to operate one server per month: $", cost_per_month)

budget = 918
days_possible = budget // cost_per_day

print("With $918, you can operate the server for", int(days_possible), "days")
