def isPowerofTwo(n):
    
    for pow in range(0,n//2):
        if 2**pow == n:
            return f"2^'{pow}'={n}"
    
    return -1

print(isPowerofTwo(1024))