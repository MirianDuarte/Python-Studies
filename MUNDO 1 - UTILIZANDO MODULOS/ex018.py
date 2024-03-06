#import math
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

#seno = math.sin(math.radians(angulo))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))

#cosseno = math.cos(math.radians(angulo))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

#tangente = math.tan(math.radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
