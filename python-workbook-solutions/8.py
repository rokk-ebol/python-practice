#8 WIDGEDTS AND GIZMOS

widget_weight =  75 
gizmo_weight = 112

widget_order = int(input('How many widgets would you like to buy?: '))
gizmo_order = int(input('How mant gizmos would you like to buy?: '))

total_weight = widget_order * widget_weight + gizmo_order * gizmo_weight

print(f"Your total order weight is {total_weight} gramms.")