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

hand32@node1:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 6500

 Performance counter stats for 'system wide':

    69,759,925,617        instructions              #    0.49  insn per cycle
   143,169,493,158        cycles
     1,026,550,403        cache-references
       173,842,003        cache-misses              #   16.935 % of all cache refs
   146,725,968,766        ref-cycles
          1,473.81 Joules power/energy-cores/
          2,764.52 Joules power/energy-pkg/
            864.79 Joules power/energy-ram/

      50.858755816 seconds time elapsed
hand32@node1:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 6500

 Performance counter stats for 'system wide':

    70,076,686,652        instructions              #    0.49  insn per cycle
   143,855,358,880        cycles
     1,030,117,575        cache-references
       177,073,847        cache-misses              #   17.190 % of all cache refs
   146,868,248,462        ref-cycles
          1,478.08 Joules power/energy-cores/
          2,769.28 Joules power/energy-pkg/
            865.54 Joules power/energy-ram/

      50.856169383 seconds time elapsed

hand32@node1:~/peakler/experiments/microbenchmarks$ perf stat -a -e instructions,cycles,cache-references,cache-misses,ref-cycles,power/energy-cores/,power/energy-pkg/,power/energy-ram/ taskset -c 15 ./build/runALU 6500

 Performance counter stats for 'system wide':

    71,151,449,075        instructions              #    0.48  insn per cycle
   146,764,211,721        cycles
     1,066,610,641        cache-references
       185,152,167        cache-misses              #   17.359 % of all cache refs
   150,685,985,840        ref-cycles
          1,493.33 Joules power/energy-cores/
          2,790.72 Joules power/energy-pkg/
            871.40 Joules power/energy-ram/

      51.280278445 seconds time elapsed

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

654960277152-15215034 = 654945062118
654945062118/10000000 = 65494
65494 = ~65000 iterations
