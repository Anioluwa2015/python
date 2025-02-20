actual_amout=float(input("write the actual amount"))
sales_amout=float(input("write the sales amount"))

if (sales_amout > actual_amout):
    profit = (sales_amout - actual_amout)
    print("profit", profit)
else:
    print("no profit")
