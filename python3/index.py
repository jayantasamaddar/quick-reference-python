# Example Code
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
new_day = input("Please add sales to Week 2:")  # 14
sales_w2.append(int(float(new_day)))
sales = sales_w1 + sales_w2
sales.sort()
print(f'Best Day: ${sales[-1] * 1.5}')          # Best Day: $63.0
print(f'Worst Day: ${sales[0] * 1.5}')          # Worst Day: $4.5
print(f'Total: ${sum(sales) * 1.5}')            # Total: $346.5