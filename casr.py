print("Car washing me aap ka sawagat hai ")
print("1:car washing")
print("2:oil change")
print("3:for Full Servicing")
Button=int(input("please select the Service (1:/2:/3:) "))
match Button:
    case 1:
        print("please pay Rs.500 only ")
    case 2:
        print("please pay Rs.1000 only ")
    case 3:
        print("please pay Rs.3200 only ")