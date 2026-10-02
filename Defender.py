customer_details={"naam":"Rahul sir","gaadi":"Defender","number":"MP 19 Na 5555"}
is_vip_customer=True
oil_price_text="4500"
brake_pad_text="8200"
labour_charge=3000
oil_price=int(oil_price_text)
brake_pad=int(brake_pad_text)
total_part_cost=oil_price+brake_pad
bill_without_tax=total_part_cost+labour_charge
gst_tax=bill_without_tax*0.18
grand_total=bill_without_tax+gst_tax
print("\n======================================")
print("     SAZ INTERNATIONAL MOTORS         ")
print("======================================")
print("customer_name:",customer_details["naam"])
print("Vechile:",customer_details["gaadi"])
print("VIP Member:", is_vip_customer)
print("----------------------------")
print("Engine oil cost:  Rs.",oil_price)
print("Brake pad cost:  Rs.",brake_pad)
print("labour charge:    Rs.", labour_charge)
print("------------------------------------")
print("Total(bina tax):Rs.",bill_without_tax)
print("gst 18%:   Rs.",gst_tax)
print("======================================")
print("GRAND TOTAL:      Rs.", grand_total)
print("======================================\n")