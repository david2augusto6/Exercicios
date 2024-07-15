from math import *

l = [0 for _ in range(13)]
f = [0 for _ in range(5)]
fn = [0 for _ in range(13)]

l[0] = l[1] = l[2] = l[3] = l[7] = 2
l[5] = l[9] = 1
l[4] = l[6] = l[10] = l[11] = l[12] = ((l[0] ** 2) + (l[5] ** 2)) ** 0.5

f[0] = f[1] = f[2] = f[3] = f[4] = 10

rAx = 0
rEx = ((f[1] * l[0] + f[2] * (l[0] + l[1]) + f[3] * (l[0] + l[1] + l[2]) + f[4] * (l[0] + l[1] + l[2] + l[3])) /
       (l[0] + l[1] + l[2] + l[3]))

rAy = f[0] + f[1] + f[2] + f[3] + f[4] - rEx

#Nó A
alpha = atan(l[5] / l[0])
fn[4] = (f[0] - rAy) / sin(alpha)
fn[0] = -rAx-fn[4]*cos(alpha)

#Nó B
fn[1] = fn[0]

#Nó F
beta = atan(l[0]/l[5])
theta = atan((l[7]-l[5])/l[1])
gama = atan(l[1] / l[5])

fn[6] = -((f[1]*cos(theta) + cos(beta)*cos(theta)*fn[4] + cos(theta)*fn[5] - fn[4]*sin(beta)*sin(theta))/(cos(gama)*cos(theta) + sin(gama)*sin(theta)))
fn[11] = (fn[6] * cos(gama) + fn[4] * cos(beta) + fn[5] + f[1]) / sin(theta)

#Nó H

psi = 1.10715
lamb = 1.10715

fn[12] = (fn[11] * sin(psi)) / sin(lamb)
fn[7] = -fn[11]*cos(psi) - fn[12]*cos(lamb) - f[2]

#Nó C
omega = 0.463648
phi = psi
delta = psi
mi = omega

fn[8] = (-fn[6] * cos(phi) - fn[7]) / cos(delta)
fn[2] = fn[1] + fn[6] * cos(omega) - fn[8] * cos(mi)

print(fn[2])

#Nó G
epsilon = l[2] / l[9]
sigma = l[3] / l[9]




print(f)
print(l)
print(fn)