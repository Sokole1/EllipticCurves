# Elliptic Curves

`curves.py` provides code to add points on an elliptic curve over a finite field.

Points on an elliptic curve satisfy the equation: $y^2 = x^3 + ax + b \bmod p$ where $a, b$, and $p$ are user specified.

You can then specify any two points on the elliptic curve by setting the variables $P1$ and $P2$, as well as the variables $k1$ and $k2$, then running `python curves.py` will compute $f(k1, k2) = k1P + k2Q$.

If you want to compute $2P1$ (point doubling) then you can simply set $P2 = P1$ and $k1 = k2 = 1$.

https://andrea.corbellini.name/ecc/interactive/modk-mul.html is also a great website that can be used to visualize and compute points on an elliptic curve.



