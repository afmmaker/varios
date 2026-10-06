"""Perfil 12 puntas (bi-hexagonal) AS870-12, DXF R12 en mm.
Union de dos hexagonos de ancho B girados 30 grados:
A = B/cos30 (puntas, 120 grados), C = B/cos15 (valles, 150 grados).
Uso: python3 genera_perfil_AS870-12.py B salida.dxf [cx cy]"""
import math, sys
B=float(sys.argv[1]); out=sys.argv[2]
cx,cy=(float(sys.argv[3]),float(sys.argv[4])) if len(sys.argv)>4 else (210.0,148.5)
RA=B/2/math.cos(math.radians(30)); RC=B/2/math.cos(math.radians(15))
pts=[(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
     for k in range(12) for r,a in ((RA,30*k),(RC,30*k+15))]
L=["0","SECTION","2","ENTITIES"]
for i,(p,q) in enumerate(zip(pts,pts[1:]+pts[:1])):
    L+=["0","LINE","8","PERFIL","10",f"{p[0]:.6f}","20",f"{p[1]:.6f}","30","0.0","11",f"{q[0]:.6f}","21",f"{q[1]:.6f}","31","0.0"]
L+=["0","POINT","8","REF","10",f"{cx}","20",f"{cy}","30","0.0","0","ENDSEC","0","EOF"]
open(out,"w").write("\n".join(L)+"\n")
print(f"B={B} A={2*RA:.3f} C={2*RC:.3f}")
