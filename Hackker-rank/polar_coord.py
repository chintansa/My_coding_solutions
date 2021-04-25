from cmath import phase
import re
line = '1-2j'
l = complex(line)
print (phase(complex(l.real,l.imag)))
print (abs(complex(l.real,l.imag)))