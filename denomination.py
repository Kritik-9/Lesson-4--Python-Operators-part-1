amount = int(input("Enter the amount to withdraw."))
note50 = amount//50
note20 = (amount%50)//20
note10 = ((amount%50)%20)//10
print(f"number of 50 notes {note50}, number of 20 notes {note20}, number of ten notes {note10}.")