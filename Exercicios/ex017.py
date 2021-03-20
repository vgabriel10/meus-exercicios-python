import math
c_a = float(input('Digite um número'))
c_o = float(input('Digite outro número'))
c_a = math.pow(c_a,2)
c_o = math.pow(c_o,2)
resp = c_a + c_o
resp_final = math.sqrt(resp)
print(resp_final)
#ou eu uso esse outro modulo mais facil
cat_o = float(input('Digite um número'))
cat_a = float(input('Digite um número'))
hipotenusa = math.hypot(cat_a,cat_o)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
