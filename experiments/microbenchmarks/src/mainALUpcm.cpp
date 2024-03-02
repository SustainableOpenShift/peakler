#include <stdio.h>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <cmath>

#include <Perf.h>
//#include <Rapl.h>

#define UINT32_MAXT 0xffffffff

/* Derived from:
[peaks@kube-worker-68 microbenchmarks]$ sudo journalctl -k --grep '^tsc:'  | cut -d' ' -f5-
[sudo] password for peaks:
kernel: tsc: Fast TSC calibration using PIT
kernel: tsc: Detected 2199.880 MHz processor
kernel: tsc: Refined TSC clocksource calibration: 2199.998 MHz
*/
#define TIME_CONVERSION_khz 2200000*1000

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
    //rapl::RaplCounter rp = rapl::RaplCounter();
    //rp.Start();
    
    uint64_t tsc_start = rdtsc();
    
    for (i=0;i<repeat_count;i++) {
      // input arguments are mostly nops, purpose is to run the 2 instructions in
      // workALU.S multiple times and ensure instruction counter makes sense
      alu(42, 3, 0);
    }

    //rp.Stop();        
    ins_retired.Stop();
    unhalted_ref_cyc_tsc.Stop();
    llc_miss.Stop();
    
    //float cpunrg = rp.ReadPkg();
    //float dramnrg = rp.ReadDram();
    uint64_t ins = ins_retired.Read();
    uint64_t ref_cyc = unhalted_ref_cyc_tsc.Read();
    uint64_t llcm = llc_miss.Read();
    
    uint64_t tsc_stop = rdtsc();
    uint64_t tsc_diff = tsc_stop - tsc_start;
    float tdiff = (tsc_diff/(float)TIME_CONVERSION_khz)/1000000.0;
    
    //rp.Clear();
    //printf("CPU: %.3lf J, DRAM: %.3lf J, TSC: %.3lf, INS: %lu, REF_CYC: %lu, LLC: %lu\n", cpunrg, dramnrg, tdiff, ins, ref_cyc, llcm);
    printf("TSC: %.3lf, INS: %lu, REF_CYC: %lu, LLC: %lu\n", tdiff, ins, ref_cyc, llcm);
    
    return 0;
}
