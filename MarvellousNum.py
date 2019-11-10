def ChkPrime(no):
    i = 2;
    prime = 1;
    while (i <= no / 2):
        if (no % i == 0):
            prime = 0;
            break;
        else:
            i += 1;

    if (prime == 1):
         return 1;
    else:
        return 0;