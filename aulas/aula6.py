"""conversão de tipos, coerção
type convertion, typecasting, coercion
é o ato de converter um tipo em outro, tipos imutáveis e primitivos: str, int, float, bool
"""
a = '0'
b = 1
c = 1.5
d = True

print(type(a), type(int(b)))

print(1 + b, type(1 + b)) #int
print(a + '1', type(a + '1')) #str -> string

z = int(a) + b #convertion str -> int
print('imprimindo z:',type(z), z)

x = float(a) + c #convertion str -> float
print('imprimindo x:', type(x), x)

y = bool(int(a)) # convertion str -> int -> bool 
print(y)