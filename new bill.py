mechanic_naam=input("Bhai,apna naam batao:")
part_ka_naam=input("kaun sa part change kiya?")
price_text=input("is part ka price kitna hai?")
asli_price=int(price_text)
gst=asli_price*0.18
grand_total=asli_price + gst
print("n/==================")
print("Live workshop bill ")
print("-------------------")
print("Mechanic:",mechanic_naam)
print("part replaced:",part_ka_naam)
print("base price:,Rs.",asli_price)
print("Gst 18%:Rs.",gst)
print("--------------------------") 
print("Grand Total:Rs.",grand_total)     

