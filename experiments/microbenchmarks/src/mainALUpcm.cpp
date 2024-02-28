#include <stdio.h>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <cmath>

#include <Perf.h>
#include <Rapl.h>

#define UINT32_MAXT 0xffffffff

/* Derived from:
sudo journalctl -k --grep '^tsc:'  | cut -d' ' -f5-
kernel: tsc: Fast TSC calibration using PIT
kernel: tsc: Detected 2599.777 MHz processor
kernel: tsc: Refined TSC clocksource calibration: 2600.000 MHz
*/
#define TIME_CONVERSION_khz 2600000*1000

extern "C" int alu(unsigned long long, unsigned long long, unsigned long long);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <repeat_count>\n", argv[0]);
        return 1;
    }

    int repeat_count = atoi(argv[1]);
    int i;

    std::unordered_map<std::string, perf::PerfCounter> counters;
    perf::PerfCounter ins_retired = perf::PerfCounter{perf::PerfEvent::fixed_instructions};
    perf::PerfCounter unhalted_ref_cyc_tsc = perf::PerfCounter{perf::PerfEvent::fixed_reference_cycles};
    perf::PerfCounter llc_miss = perf::PerfCounter{perf::PerfEvent::llc_misses};
    
    ins_retired.Start();
    unhalted_ref_cyc_tsc.Start();
    llc_miss.Start();
    rapl::RaplCounter rp = rapl::RaplCounter();
    rp.Start();
    
    uint64_t tsc_start = rdtsc();
    
    for (i=0;i<repeat_count;i++) {
      // input arguments are mostly nops, purpose is to run the 2 instructions in
      // workALU.S multiple times and ensure instruction counter makes sense
      alu(42, 3, 0);
    }

    rp.Stop();        
    ins_retired.Stop();
    unhalted_ref_cyc_tsc.Stop();
    llc_miss.Stop();
    
    float nrg = rp.Read();
    uint64_t ins = ins_retired.Read();
    uint64_t ref_cyc = unhalted_ref_cyc_tsc.Read();
    uint64_t llcm = llc_miss.Read();
    
    uint64_t tsc_stop = rdtsc();
    uint64_t tsc_diff = tsc_stop - tsc_start;
    float tdiff = (tsc_diff/(float)TIME_CONVERSION_khz)/1000000.0;
    
    rp.Clear();
    printf("%.3lf J,%.3lf, ins=%lu, ref_cyc=%lu, llcm=%lu\n", nrg, tdiff, ins, ref_cyc, llcm);
    
    return 0;
}
