'''

What is the time, space complexity of following code :

    int a = 0, b = 0;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            a = a + j;
        }
    }
    for (k = 0; k < N; k++) {
        b = b + k;
    }

 O(N * N) time, O(1) space
 O(N) time, O(N) space
 O(N) time, O(N) space
 O(N * N) time, O(N) space
 O(N * N * N) time, O(1) space

'''

O(N * N) time, O(1) space

The first set of nested loops is O(N^2) and the second loop is O(N).

This is O(max(N^2,N)) which is O(N^2).