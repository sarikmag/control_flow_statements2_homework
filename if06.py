def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    s=n//1000%10
    d=n//100%10
    f=n//10%10
    g=n%10
    if a>s and a>d and a>f and a>g:
        return 5
    if s>a and s>d and s>f and s>g:
        return 4 
    if d>a and d>s and d>f and d>g:
        return 3 
    if f>a and f>s and f>d and f>g:
        return 2 
    if g>a and g>s and g>d and g>f:
        return 1
print(main(76514))