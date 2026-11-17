tuition_fee=float(input("Enter tuition fee:"))
lab_fee=float(input("Enter lab fee:"))
library_fee=float(input("Enter library fee:"))
exam_fee=float(input("Enter exam fee:"))
discount=float(input("enter discount amount:"))
total_fee=tuition_fee+lab_fee+library_fee+exam_fee
fee_after_discount=total_fee-discount
annual_fee=fee_after_discount*2
monthly_installment=annual_fee/12
print("\ntuition_fee:",tuition_fee)
print("lab fee:",lab_fee)
print("library fee:",library_fee)
print("exam fee:",exam_fee)
print("discount:",discount)
print("fee after discount:",fee_after_discount)
print("annual fee:",annual_fee)
print("monthly installment:",round(monthly_installment,2))
