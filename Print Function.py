if __name__ == '__main__':
    n = int(input())
    
    result = 1
    m = 10
    
    for i in range(n+1):
        if i <= 1:
            pass
        else:
            if i % m == 0:
                m *= 10
            result = m * result + i

    print(result)
