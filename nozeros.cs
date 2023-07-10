using System;

public class NoBoring
{
    public static int NoBoringZeros(int n)
    {
        while (n % 10 == 0 && n != 0)
        {
            n /= 10;
        }

        return n;
    }
}
