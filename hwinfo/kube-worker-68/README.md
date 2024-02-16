# Hardware info for this node

```
$ cat /proc/cpuinfo
processor	: 87
vendor_id	: GenuineIntel
cpu family	: 6
model		: 79
model name	: Intel(R) Xeon(R) CPU E5-4669 v4 @ 2.20GHz
stepping	: 1
microcode	: 0xb000040
cpu MHz		: 1200.000
cache size	: 56320 KB
physical id	: 3
siblings	: 22
core id		: 28
cpu cores	: 22
apicid		: 248
initial apicid	: 248
fpu		: yes
fpu_exception	: yes
cpuid level	: 20
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a rdseed adx smap intel_pt xsaveopt cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts md_clear flush_l1d
vmx flags	: vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs pml
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs taa itlb_multihit mmio_stale_data
bogomips	: 4410.67
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:

$ numactl --hardware
available: 4 nodes (0-3)
node 0 cpus: 0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84
node 0 size: 515920 MB
node 0 free: 513248 MB
node 1 cpus: 1 5 9 13 17 21 25 29 33 37 41 45 49 53 57 61 65 69 73 77 81 85
node 1 size: 516045 MB
node 1 free: 509456 MB
node 2 cpus: 2 6 10 14 18 22 26 30 34 38 42 46 50 54 58 62 66 70 74 78 82 86
node 2 size: 516084 MB
node 2 free: 512018 MB
node 3 cpus: 3 7 11 15 19 23 27 31 35 39 43 47 51 55 59 63 67 71 75 79 83 87
node 3 size: 516076 MB
node 3 free: 514513 MB
node distances:
node   0   1   2   3
  0:  10  21  31  21
  1:  21  10  21  31
  2:  31  21  10  21
  3:  21  31  21  10

$ free -h
               total        used        free      shared  buff/cache   available
Mem:           2.0Ti       3.7Gi       2.0Ti        16Mi        10Gi       2.0Ti
Swap:             0B          0B          0B

$ df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       1.4T   11G  1.3T   1% /

$ lshw -c network
product: MT27710 Family [ConnectX-4 Lx]
vendor: Mellanox Technologies
size: 25Gbit/s
capacity: 25Gbit/s
```