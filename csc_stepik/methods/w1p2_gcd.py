
def euclid_gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    
    if a >= b:
        return euclid_gcd(a % b, b)
    else:
        return euclid_gcd(a, b % a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    print(euclid_gcd(a, b))
