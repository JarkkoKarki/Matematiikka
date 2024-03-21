import numpy as np
a = 2.493
b = 0.911
c = 137.7
d = 62.3
print("Tehtävä 1")
print(f"A: {np.degrees(a):.3f}{u'\N{DEGREE SIGN}'}")
print(f"B: {np.degrees(b):.3f}{u'\N{DEGREE SIGN}'}")
print("Tehtävä 2")
print(f"A:{np.radians(c):.5f}")
print(f"A:{np.radians(d):.5f}")
print("Tehtävä 3")
e_degree = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
e_radian = []
for i in e_degree:
    e_radian.append(float(f"{np.radians(i):.5f}"))
print(e_degree)
print(e_radian)
print("Tehtävä 4")
sivu1 = 1.6
sivu2 =2.3
print(f"{np.hypot(sivu1, sivu2):.2f}m")
