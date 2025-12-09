# Define the elliptic curve parameters with variables: y^2 = x^3 + ax + b mod p
a = 2
b = 4
p = 13

# Check if curve is non-singular
if (4 * a**3 + 27 * b**2) % p == 0:
    raise ValueError("Invalid curve, choose different a and b.")

# Define points P1 and P2 and choose scalars k1 and k2 to compute P3 = k1*P1 + k2*P2
P1 = (5, 3)
P2 = (0, 2)
k1 = 2
k2 = 1

if k1 < 1 or k2 < 1 or not isinstance(k1, int) or not isinstance(k2, int):
    raise ValueError("k1 and k2 must be positive integers")

# Check if P1 and P2 are on the curve
def validate_points(P):
    # Throw error if point is not on the curve
    (x, y) = P
    if (x**3 + a*x + b) % p != (y**2) % p:
        raise ValueError(f"Point {P} is not on the curve.")

validate_points(P1)
validate_points(P2)

def point_addition(P, Q):
    (xp, yp) = P
    (xq, yq) = Q

    if P != Q:
        if xp == xq:
            return None  # Point at infinity

        # Note : Modular division is multiplication by modular inverse
        lmbda = (yq - yp) * pow(xq - xp, -1, p) % p
    else:
        if yp == 0:
            return None  # Point at infinity

        lmbda = (3 * xp**2 + a) * pow(2 * yp, -1, p) % p
    
    x3 = (lmbda**2 - xp - xq) % p
    y3 = (lmbda * (xp - x3) - yp) % p
    
    return (x3, y3)

# Compute kP, return None if it equals 0 - the point at infinity
def compute_kP(k, P):
    if k == 0:
        return None # Point at infinity
    if P == None:
        return None

    Pk = P
    for _ in range(k - 1):
        if Pk == None:
            Pk = P # Since P + 0 = P by definition
        else:
            Pk = point_addition(P, Pk)
        
    return Pk

# This is our quantum oracle f, which computes k1*P1 + k2*P2
# Using discrete logarithm notation, this compute f(k1, k2) = (P1^k1)(P2^k2)
def compute_k1Pk2Q(k1, P, k2, Q):
    k1P = compute_kP(k1, P)
    k2Q = compute_kP(k2, Q)

    if k1P == None:
        return k2Q
    if k2Q == None:
        return k1P

    return point_addition(k1P, k2Q)

compute_k1Pk2Q(k1, P1, k2, P2)

print("k1P1 + k2P2 =", compute_k1Pk2Q(k1, P1, k2, P2))