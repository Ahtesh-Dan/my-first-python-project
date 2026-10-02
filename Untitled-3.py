paint_color = "Matte black"
paint_dabba_price = "5500"
labour_hours = 4.5
per_hour_Rate = 1000

asli_paint_price = int(paint_dabba_price)

# PICHHLI BAAR AAP YE CALCULATION WALI 2 LINES BHOOL GAYE THE!
total_labour_cost = labour_hours * per_hour_Rate
grand_total = asli_paint_price + total_labour_cost

# Ab jab dabbe ban gaye hain, tab hum unhe print karenge
print("-------Paint job bill------")
print("paint color: ", paint_color)
print("paint cost:Rs.", asli_paint_price)
print("labour cost:Rs.", total_labour_cost)
print("---------------------------")
print("Grand total:RS.", grand_total)