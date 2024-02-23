#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int memc(char*, char*, int, int);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <repeat_count>\n", argv[0]);
        return 1;
    }

    int repeat_count = atoi(argv[1]);
    int i;
    
    unsigned int num_elements = (0x1 << 22); // 40 MB ==  ~(2 * L3 cache)
    char *aa, *bb;
    
    aa = (char*) malloc (num_elements * sizeof(char));
    bb = (char*) malloc (num_elements * sizeof(char));
    
    memset(aa, 'a', num_elements*sizeof(char));
    memset(bb, 'b', num_elements*sizeof(char));
    
    for(i=0;i<repeat_count;i++) {
      // copies from bb to aa
      memc(aa, bb, num_elements, num_elements);
    }
    
    printf("%c %c\n", aa[num_elements-10], bb[num_elements-10]);
    
    return 0;
}

