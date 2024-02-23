#include <stdio.h>
#include <stdlib.h>

extern int alu(unsigned long long, unsigned long long, unsigned long long);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <repeat_count>\n", argv[0]);
        return 1;
    }

    int repeat_count = atoi(argv[1]);
    int i;

    for (i=0;i<repeat_count;i++) {
      // input arguments are mostly nops, purpose is to run the 2 instructions in
      // workALU.S multiple times and ensure instruction counter makes sense
      alu(42, 3, 0);
    }

    return 0;
}
