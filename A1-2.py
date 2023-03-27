gi=float(input("Your Gross Income is "))
du=int(input("Dependent users in your family are "))
sd=10000
ti=gi-sd-(3000*du)
t=ti*0.2
print("Tax Payable =",t)
