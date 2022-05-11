# Gross & Net pay entries
gp1 = int(input("Check #1 Gross: $"))
np1 = int(input("Check #1 Net: $"))
gp2 = int(input("Check #2 Gross: $"))
np2 = int(input("Check #2 Net: $"))
more_input = input("Do you want to enter more pay entries? Y/N  ")

gross_pay = gp1 + gp2
net_pay = np1 + np2
tax_paid = gross_pay - net_pay
tax_rate = (tax_paid / gross_pay) * 100

if more_input == "Y" or more_input == "y":
    gp3 = int(input("Check #3 Gross: $"))
    np3 = int(input("Check #3 Net: $"))
    gross_pay = gp1 + gp2 + gp3
    net_pay = np1 + np2 + np3
    more_input = input("Do you want to enter more pay entries? Y/N  ")

    if more_input == "Y" or more_input == "y":
        gp4 = int(input("Check #4 Gross: $"))
        np4 = int(input("Check #4 Net: $"))
        gross_pay = gp1 + gp2 + gp3 + gp4
        net_pay = np1 + np2 + np3 + np4
        more_input = input("Do you want to enter more pay entries? Y/N  ")

        if more_input == "Y" or more_input == "y":
            gp5 = int(input("Check #5 Gross: $"))
            np5 = int(input("Check #5 Net: $"))
            gross_pay = gp1 + gp2 + gp3 + gp4 + gp5
            net_pay = np1 + np2 + np3 + np4 + np5
        else:
            pass
    else:
        pass
else:
    pass

# Calcs
print("You've grossed $", gross_pay, "this year.")
print("You've netted $", net_pay, "this year.")
print("Tax Rate: ", round(tax_rate,2), "%")