# results

```
hand32@Mapper10-3:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 1

Performance counter stats for 'system wide':

        25,415,217        instructions              #    0.59  insn per cycle         
        43,439,470        cycles                                                      
           340,938        cache-references                                            
            69,277        cache-misses              #   20.320 % of all cache refs    
        59,816,796        ref-cycles                                                  
              0.44 Joules power/energy-cores/                                         
              0.99 Joules power/energy-pkg/                                           
              0.26 Joules power/energy-ram/                                           

       0.021176049 seconds time elapsed

hand32@Mapper10-3:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 2

 Performance counter stats for 'system wide':

        35,493,137        instructions              #    0.51  insn per cycle         
        69,396,668        cycles                                                      
           507,669        cache-references                                            
           103,203        cache-misses              #   20.329 % of all cache refs    
        84,723,262        ref-cycles                                                  
              0.67 Joules power/energy-cores/                                         
              1.42 Joules power/energy-pkg/                                           
              0.37 Joules power/energy-ram/                                           

       0.030234016 seconds time elapsed


hand32@Mapper10-3:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 3

 Performance counter stats for 'system wide':

        45,546,367        instructions              #    0.49  insn per cycle         
        92,950,534        cycles                                                      
           660,462        cache-references                                            
           126,312        cache-misses              #   19.125 % of all cache refs    
       110,020,872        ref-cycles                                                  
              0.89 Joules power/energy-cores/                                         
              1.88 Joules power/energy-pkg/                                           
              0.47 Joules power/energy-ram/                                           

       0.039708530 seconds time elapsed

hand32@Mapper10-3:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 6500

 Performance counter stats for 'system wide':

    65,387,646,182        instructions              #    0.43  insn per cycle         
   153,475,542,779        cycles                                                      
       986,226,116        cache-references                                            
       142,910,907        cache-misses              #   14.491 % of all cache refs    
   154,371,409,322        ref-cycles                                                  
          1,404.72 Joules power/energy-cores/                                         
          2,884.02 Joules power/energy-pkg/                                           
            703.80 Joules power/energy-ram/                                           

      58.678943883 seconds time elapsed

hand32@Mapper10-3:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 65000

 Performance counter stats for 'system wide':

   654,960,277,152        instructions              #    0.43  insn per cycle         
 1,536,131,780,811        cycles                                                      
     9,875,089,991        cache-references                                            
     1,430,615,511        cache-misses              #   14.487 % of all cache refs    
 1,545,756,709,692        ref-cycles                                                  
         14,112.74 Joules power/energy-cores/                                         
         28,962.41 Joules power/energy-pkg/                                           
          7,239.28 Joules power/energy-ram/                                           

     586.800554147 seconds time elapsed

```
## Assuming 10,000,000 instructions, then there is around 25,415,217 - 10,000,000 = 15,215,034 non work ALU instructions
## 