# 6 TAX AND TIP

tax_rate = 0.20
tip = 0.18

order = float(input('On what sum did you just order?: '))
checkout = order + order * tax_rate + order * tip

print('Checkout is: %.2f $' % checkout)