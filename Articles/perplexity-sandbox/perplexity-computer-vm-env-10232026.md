# Full system inventory of the Perplexity Computer VM

*By **Elias Bachaalany** — [@0xeb](https://github.com/0xeb) on GitHub · [Binary Wizards](https://www.youtube.com/@binary-wizards) on YouTube · [@eliasbchlny](https://x.com/eliasbchlny) on X*

Perplexity Computer runs on a **VM**. Behind the answer engine is a real Linux machine with a shell, a package manager, compilers, an office suite, and a headless X desktop. The agent can write and run code there, convert and generate documents, drive GUI applications, and keep files on disk for the length of the session.

So the same question I asked about the [ChatGPT Work VM](../chatgpt-sandbox/chatgpt-work-vm-env-08062026.md) applies here: **what is the machine?** How many cores, how much RAM, how much disk, what is preinstalled, and what does the agent run as? This is the full inventory: CPU, memory, storage, cgroup limits, mounts, devices, privileges, toolchains, the desktop stack, and the complete Debian, Python, and Node package lists.

*Captured **2026-10-23 03:05:48 UTC** from a live session. Every figure below is a reading taken at that moment, not the model's recollection of its own environment. No environment-variable values, credentials, network addresses, or machine identifiers were collected.*

> **Not a pristine image.** SWI-Prolog and its dependencies were installed earlier in the same conversation, so they appear in the package lists below. Everything else is what the session came with.

## Practical capacity, up front

If you are sizing up what to run in this thing, the useful limits are:

- **2 vCPUs** (Intel Xeon, Ice Lake-SP class, AVX-512)
- **7.8 GiB guest RAM**, with a cgroup ceiling of **7.646 GiB** (`memory.max` = 8,210,063,360 bytes)
- **No swap**
- **20 GB ext4 root disk**, about **13 GB available**
- **Passwordless `sudo`**, so you can `apt install` whatever is missing
- **847 Debian packages**, **145 Python distributions**, and a handful of global Node CLIs
- A **headless desktop stack**: Xvfb, Openbox, xfce4-panel, Alacritty, plus the full LibreOffice suite
- **No** GPU, Docker/Podman, clang, CMake, Ninja, gdb, Java, Go, or Rust preinstalled

This is a small box. It is good for document work (office files, PDFs, OCR, media conversion), scripting in Python/Node, and small C/C++ builds. It is not the place for heavy parallel builds or anything that needs more than ~7 GiB of RAM. Because you have root, most missing tools are one `sudo apt install` away, which is how SWI-Prolog got there.

The rest of this article is the evidence behind those numbers.

## Important scope note

This describes the **execution sandbox** used for shell commands, not the infrastructure that serves the language model. Physical host resources, model weights, inference accelerators, and any external tool-service machines are not observable from inside it.

Unlike the ChatGPT Work VM, this guest **does not hide `/proc` and `/sys`**. Standard tools such as `lscpu`, `free`, `df`, and `lsblk` work normally, and the raw output is reproduced below.

Resource usage is a point-in-time reading. A device node or an installed package does not by itself prove that a physical device is attached or that a service is running.

## Operating system

| Item | Value |
|---|---|
| Distribution | Ubuntu 26.04.1 LTS |
| Codename | Resolute Raccoon |
| Kernel | Linux 6.1.155 |
| Kernel build | `#1 SMP PREEMPT_DYNAMIC @1760348006` |
| Architecture | x86_64 |
| Virtualization | KVM (full) |
| Hostname | `space-sandbox` |
| User | `uid=2000(user) gid=2000(user) groups=2000(user)` |
| Init | systemd 259.5 |

The userland is very new (Ubuntu 26.04, GCC 15, Python 3.14), but the kernel is a **6.1 LTS** build. That is a custom guest kernel supplied by the VM platform, not Ubuntu's stock kernel. The `space-sandbox` hostname and the `space.slice` cgroup (see below) are the only Perplexity-specific names at the OS level.

```text
Linux space-sandbox 6.1.155 #1 SMP PREEMPT_DYNAMIC @1760348006 x86_64 GNU/Linux
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
uid=2000(user) gid=2000(user) groups=2000(user)
```

## CPU

| Item | Value |
|---|---|
| Assigned processors | 2 vCPUs (IDs 0–1) |
| Model name | Intel Xeon Processor @ 2.90 GHz |
| Family / model / stepping | 6 / 106 / 6 (Ice Lake-SP) |
| Threads per core | 1 |
| Cores per socket / sockets | 2 / 1 |
| Address sizes | 46 bits physical, 57 bits virtual |
| L1d / L1i | 96 KiB / 64 KiB (2 instances) |
| L2 | 2.5 MiB (2 instances) |
| L3 | 54 MiB (1 instance) |
| NUMA nodes | 1 |
| Hypervisor | KVM |

Family 6 model 106 is **Ice Lake-SP** (3rd-gen Xeon Scalable). The model string is generic ("Intel(R) Xeon(R) Processor"), which is typical of cloud guests that mask the exact SKU. One thread per core means no SMT siblings are exposed to the guest.

Exposed instruction support includes SSE through SSE4.2, AVX, AVX2, FMA, BMI1/2, AES, PCLMUL, VAES, VPCLMULQDQ, SHA-NI, GFNI, RDRAND, RDSEED, and AVX-512 F, DQ, CD, BW, VL, IFMA, VBMI, VBMI2, VNNI, BITALG, and VPOPCNTDQ. The guest reports standard mitigations for Spectre v1/v2, Speculative Store Bypass, and MMIO stale data, with TSX disabled.

Full `lscpu` output:

```text
Architecture:                            x86_64
CPU op-mode(s):                          32-bit, 64-bit
Address sizes:                           46 bits physical, 57 bits virtual
Byte Order:                              Little Endian
CPU(s):                                  2
On-line CPU(s) list:                     0,1
Vendor ID:                               GenuineIntel
Model name:                              Intel(R) Xeon(R) Processor @ 2.90GHz
CPU family:                              6
Model:                                   106
Thread(s) per core:                      1
Core(s) per socket:                      2
Socket(s):                               1
Stepping:                                6
BogoMIPS:                                5799.92
Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc pebs bts rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq dtes64 ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm md_clear flush_l1d arch_capabilities
Hypervisor vendor:                       KVM
Virtualization type:                     full
L1d cache:                               96 KiB (2 instances)
L1i cache:                               64 KiB (2 instances)
L2 cache:                                2.5 MiB (2 instances)
L3 cache:                                54 MiB (1 instance)
NUMA node(s):                            1
NUMA node0 CPU(s):                       0,1
Vulnerability Gather data sampling:      Not affected
Vulnerability Indirect target selection: Mitigation; Aligned branch/return thunks
Vulnerability Itlb multihit:             Not affected
Vulnerability L1tf:                      Not affected
Vulnerability Mds:                       Not affected
Vulnerability Meltdown:                  Not affected
Vulnerability Mmio stale data:           Mitigation; Clear CPU buffers; SMT Host state unknown
Vulnerability Reg file data sampling:    Not affected
Vulnerability Retbleed:                  Not affected
Vulnerability Spec rstack overflow:      Not affected
Vulnerability Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:                Mitigation; Enhanced / Automatic IBRS; IBPB conditional; PBRSB-eIBRS SW sequence; BHI SW loop, KVM SW loop
Vulnerability Srbds:                     Not affected
Vulnerability Tsa:                       Not affected
Vulnerability Tsx async abort:           Mitigation; TSX disabled
Vulnerability Vmscape:                   Not affected
```

## Memory and storage

| Item | Value |
|---|---:|
| Total RAM | 7.8 GiB |
| Used at capture | 345 MiB |
| Free | 7.2 GiB |
| Available | 7.4 GiB |
| Swap | 0 |
| Root filesystem | `/dev/root` (ext4 on `vda`), 20 GB |
| Root used / available | 6.7 GB / 13 GB (35%) |
| `/dev/shm` (tmpfs) | 3.9 GiB |
| `/run` (tmpfs) | 1.6 GiB |

**No swap.** Whatever you run either fits in roughly 7.6 GiB or the cgroup OOM-kills it. The root disk is a single virtio block device, and a third of it is already used by the base image.

```text
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       345Mi       7.2Gi       6.8Mi       526Mi       7.4Gi
Swap:             0B          0B          0B
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/root      ext4    20G  6.7G   13G  35% /
tmpfs          tmpfs  3.9G     0  3.9G   0% /dev/shm
tmpfs          tmpfs  1.6G  6.1M  1.6G   1% /run
NAME TYPE SIZE FSTYPE MOUNTPOINTS MODEL
vda  disk  20G        /           
```

## Cgroup resource limits

The workload runs inside a two-level cgroup v2 hierarchy:

| Limit | `space.slice` | `space-workloads.service/workloads` |
|---|---:|---:|
| `memory.max` | 8,210,063,360 (7.646 GiB) | 8,210,063,360 (7.646 GiB) |
| `memory.current` | 438,935,552 | 429,068,288 |
| `memory.swap.max` | max | max |
| `cpu.max` | max 100000 (no quota) | max 100000 (no quota) |
| `cpuset.cpus.effective` | 0-1 | — |
| `pids.max` | 32,000 | 28,000 |

There is no CPU quota, so you get both vCPUs at full speed. The real ceilings are memory and process count.

```text

/sys/fs/cgroup/space.slice
memory.max: 8210063360
memory.current: 438935552
memory.swap.max: max
cpu.max: max 100000
cpuset.cpus.effective: 0-1
pids.max: 32000

/sys/fs/cgroup/space.slice/space-workloads.service/workloads
memory.max: 8210063360
memory.current: 429068288
memory.swap.max: max
cpu.max: max 100000
pids.max: 28000
```

## Mounts

A conventional systemd guest: an ext4 root on `/dev/vda`, with `proc`, `sysfs`, and a `cgroup2` hierarchy mounted normally. `securityfs`, `selinuxfs`, `bpf`, `tracefs`, and `pstore` are also mounted. Nothing here is a bind-mounted overlay or a hidden pseudo-filesystem, which is quite different from the locked-down ChatGPT box.

```text
/ /dev/vda ext4 rw,relatime
/dev devtmpfs devtmpfs rw,relatime,size=4071212k,nr_inodes=1017803,mode=755
/proc proc proc rw,nosuid,nodev,noexec,relatime
/sys sysfs sysfs rw,nosuid,nodev,noexec,relatime
/sys/kernel/security securityfs securityfs rw,nosuid,nodev,noexec,relatime
/sys/fs/selinux selinuxfs selinuxfs rw,nosuid,noexec,relatime
/dev/shm tmpfs tmpfs rw,nosuid,nodev
/dev/pts devpts devpts rw,nosuid,noexec,relatime,gid=5,mode=600,ptmxmode=000
/run tmpfs tmpfs rw,nosuid,nodev,size=1629744k,nr_inodes=819200,mode=755
/sys/fs/cgroup cgroup2 cgroup2 rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot
/sys/fs/pstore pstore pstore rw,nosuid,nodev,noexec,relatime
/sys/fs/bpf bpf bpf rw,nosuid,nodev,noexec,relatime,mode=700
/proc/sys/fs/binfmt_misc systemd-1 autofs rw,relatime,fd=35,pgrp=1,timeout=0,minproto=5,maxproto=5,direct
/sys/kernel/tracing tracefs tracefs rw,nosuid,nodev,noexec,relatime
/run/credentials/systemd-journald.service none ramfs ro,nosuid,nodev,noexec,relatime,nosymfollow,mode=700
```

## Devices

- **No PCI or USB devices** are enumerated, and there are **no GPU device nodes**.
- Three **virtio** devices: `virtio_blk` (the root disk), `virtio_net`, and `vmw_vsock_virtio_transport` (a host↔guest vsock channel, typically used by the orchestrator to talk to an in-guest agent).
- An emulated **AT Raw Set 2 keyboard**.
- `/dev/vmclock0`, `/dev/sysgenid`, and `/dev/ptp0`. These are VM clock and generation-ID devices used by **snapshot/restore-capable microVM platforms**. They let a guest notice it has been cloned or resumed from a snapshot and resync its clock and random state. Together with the absence of PCI, this points to a Firecracker-style microVM restored from a warm snapshot, rather than a conventional full VM.

```text
PCI:

USB:

Virtio drivers:
virtio0: ../../../../bus/virtio/drivers/virtio_blk
virtio1: ../../../../bus/virtio/drivers/virtio_net
virtio2: ../../../../bus/virtio/drivers/vmw_vsock_virtio_transport

Input device:
AT Raw Set 2 keyboard

Device nodes:
total 0
crw-r--r-- 1 root root  10, 235 Oct 22 22:37 autofs
crw------- 1 root root   5,   1 Oct 23 03:04 console
lrwxrwxrwx 1 root root      11 Oct 22 22:37 core -> /proc/kcore
drwxr-xr-x 4 root root      80 Oct 22 22:37 cpu
crw------- 1 root root  10, 122 Oct 22 22:37 cpu_dma_latency
lrwxrwxrwx 1 root root      13 Oct 22 22:37 fd -> /proc/self/fd
crw-rw-rw- 1 root root   1,   7 Oct 22 22:37 full
crw------- 1 root root  10, 183 Oct 22 22:37 hwrng
drwxr-xr-x 2 root root      60 Oct 22 22:37 input
crw-r--r-- 1 root root   1,  11 Oct 22 22:37 kmsg
lrwxrwxrwx 1 root root      28 Oct 22 22:37 log -> /run/systemd/journal/dev-log
crw-rw---- 1 root disk  10, 237 Oct 22 22:37 loop-control
brw------- 1 root root   7,   0 Oct 22 22:37 loop0
brw------- 1 root root   7,   1 Oct 22 22:37 loop1
brw------- 1 root root   7,   2 Oct 22 22:37 loop2
brw------- 1 root root   7,   3 Oct 22 22:37 loop3
brw------- 1 root root   7,   4 Oct 22 22:37 loop4
brw------- 1 root root   7,   5 Oct 22 22:37 loop5
brw------- 1 root root   7,   6 Oct 22 22:37 loop6
brw------- 1 root root   7,   7 Oct 22 22:37 loop7
crw------- 1 root root   1,   1 Oct 22 22:37 mem
crw-rw-rw- 1 root root   1,   3 Oct 22 22:37 null
crw------- 1 root root   1,   4 Oct 22 22:37 port
crw-rw-rw- 1 root root   5,   2 Oct 22 22:37 ptmx
crw------- 1 root root 250,   0 Oct 22 22:37 ptp0
drwxr-xr-x 2 root root       0 Oct 22 22:37 pts
crw-rw-rw- 1 root root   1,   8 Oct 22 22:37 random
drwxrwxrwt 2 root root      40 Oct 22 22:37 shm
crw------- 1 root root  10, 231 Oct 22 22:37 snapshot
lrwxrwxrwx 1 root root      15 Oct 22 22:37 stderr -> /proc/self/fd/2
lrwxrwxrwx 1 root root      15 Oct 22 22:37 stdin -> /proc/self/fd/0
lrwxrwxrwx 1 root root      15 Oct 22 22:37 stdout -> /proc/self/fd/1
crw------- 1 root root  10, 125 Oct 22 22:37 sysgenid
crw-rw-rw- 1 root root   5,   0 Oct 22 22:37 tty
crw------- 1 root root   4,   0 Oct 22 22:37 tty0
crw------- 1 root root   4,   1 Oct 22 22:37 tty1
crw------- 1 root root   4,  10 Oct 22 22:37 tty10
crw------- 1 root root   4,  11 Oct 22 22:37 tty11
crw------- 1 root root   4,  12 Oct 22 22:37 tty12
crw------- 1 root root   4,  13 Oct 22 22:37 tty13
crw------- 1 root root   4,  14 Oct 22 22:37 tty14
crw------- 1 root root   4,  15 Oct 22 22:37 tty15
crw------- 1 root root   4,  16 Oct 22 22:37 tty16
crw------- 1 root root   4,  17 Oct 22 22:37 tty17
crw------- 1 root root   4,  18 Oct 22 22:37 tty18
crw------- 1 root root   4,  19 Oct 22 22:37 tty19
crw------- 1 root root   4,   2 Oct 22 22:37 tty2
crw------- 1 root root   4,  20 Oct 22 22:37 tty20
crw------- 1 root root   4,  21 Oct 22 22:37 tty21
crw------- 1 root root   4,  22 Oct 22 22:37 tty22
crw------- 1 root root   4,  23 Oct 22 22:37 tty23
crw------- 1 root root   4,  24 Oct 22 22:37 tty24
crw------- 1 root root   4,  25 Oct 22 22:37 tty25
crw------- 1 root root   4,  26 Oct 22 22:37 tty26
crw------- 1 root root   4,  27 Oct 22 22:37 tty27
crw------- 1 root root   4,  28 Oct 22 22:37 tty28
crw------- 1 root root   4,  29 Oct 22 22:37 tty29
crw------- 1 root root   4,   3 Oct 22 22:37 tty3
crw------- 1 root root   4,  30 Oct 22 22:37 tty30
crw------- 1 root root   4,  31 Oct 22 22:37 tty31
crw------- 1 root root   4,  32 Oct 22 22:37 tty32
crw------- 1 root root   4,  33 Oct 22 22:37 tty33
crw------- 1 root root   4,  34 Oct 22 22:37 tty34
crw------- 1 root root   4,  35 Oct 22 22:37 tty35
crw------- 1 root root   4,  36 Oct 22 22:37 tty36
crw------- 1 root root   4,  37 Oct 22 22:37 tty37
crw------- 1 root root   4,  38 Oct 22 22:37 tty38
crw------- 1 root root   4,  39 Oct 22 22:37 tty39
crw------- 1 root root   4,   4 Oct 22 22:37 tty4
crw------- 1 root root   4,  40 Oct 22 22:37 tty40
crw------- 1 root root   4,  41 Oct 22 22:37 tty41
crw------- 1 root root   4,  42 Oct 22 22:37 tty42
crw------- 1 root root   4,  43 Oct 22 22:37 tty43
crw------- 1 root root   4,  44 Oct 22 22:37 tty44
crw------- 1 root root   4,  45 Oct 22 22:37 tty45
crw------- 1 root root   4,  46 Oct 22 22:37 tty46
crw------- 1 root root   4,  47 Oct 22 22:37 tty47
crw------- 1 root root   4,  48 Oct 22 22:37 tty48
crw------- 1 root root   4,  49 Oct 22 22:37 tty49
crw------- 1 root root   4,   5 Oct 22 22:37 tty5
crw------- 1 root root   4,  50 Oct 22 22:37 tty50
crw------- 1 root root   4,  51 Oct 22 22:37 tty51
crw------- 1 root root   4,  52 Oct 22 22:37 tty52
crw------- 1 root root   4,  53 Oct 22 22:37 tty53
crw------- 1 root root   4,  54 Oct 22 22:37 tty54
crw------- 1 root root   4,  55 Oct 22 22:37 tty55
crw------- 1 root root   4,  56 Oct 22 22:37 tty56
crw------- 1 root root   4,  57 Oct 22 22:37 tty57
crw------- 1 root root   4,  58 Oct 22 22:37 tty58
crw------- 1 root root   4,  59 Oct 22 22:37 tty59
crw------- 1 root root   4,   6 Oct 22 22:37 tty6
crw------- 1 root root   4,  60 Oct 22 22:37 tty60
crw------- 1 root root   4,  61 Oct 22 22:37 tty61
crw------- 1 root root   4,  62 Oct 22 22:37 tty62
crw------- 1 root root   4,  63 Oct 22 22:37 tty63
crw------- 1 root root   4,   7 Oct 22 22:37 tty7
crw------- 1 root root   4,   8 Oct 22 22:37 tty8
crw------- 1 root root   4,   9 Oct 22 22:37 tty9
crw-rw-rw- 1 root root   1,   9 Oct 22 22:37 urandom
crw------- 1 root root  10, 126 Oct 22 22:37 userfaultfd
crw------- 1 root root   7,   0 Oct 22 22:37 vcs
crw------- 1 root root   7,   1 Oct 22 22:37 vcs1
crw------- 1 root root   7, 128 Oct 22 22:37 vcsa
crw------- 1 root root   7, 129 Oct 22 22:37 vcsa1
crw------- 1 root root   7,  64 Oct 22 22:37 vcsu
crw------- 1 root root   7,  65 Oct 22 22:37 vcsu1
brw------- 1 root root 254,   0 Oct 22 22:37 vda
crw------- 1 root root  10, 127 Oct 22 22:37 vga_arbiter
crw------- 1 root root  10, 124 Oct 22 22:37 vmclock0
crw------- 1 root root  10, 123 Oct 22 22:37 vsock
crw-rw-rw- 1 root root   1,   5 Oct 22 22:37 zero

GPU nodes:
```

## Privileges and process resource limits

The sandbox user has **passwordless `sudo`**, so the agent is effectively root inside the VM. That is the biggest practical difference from the ChatGPT Work VM: here `apt install` just works.

| Limit | Value |
|---|---:|
| Open files | 4,096 |
| Max user processes | 31,806 |
| Pending signals | 31,806 |
| Stack | 8 MiB |
| Max locked memory | 8 MiB |
| Core file size | 0 (disabled) |
| CPU time / virtual memory / file size | unlimited |

```text
Passwordless sudo available in sandbox
real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 31806
max locked memory           (kbytes, -l) 8192
max memory size             (kbytes, -m) unlimited
open files                          (-n) 4096
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 31806
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```

## Main development software

| Software | Version | Path |
|---|---|---|
| GCC / G++ | 15.2.0 (Ubuntu 15.2.0-16ubuntu1) | `/usr/bin/gcc`, `/usr/bin/g++` |
| GNU Make | 4.4.1 | `/usr/bin/make` |
| Python | 3.14.8 (`/usr/local` build) and 3.14.4 (distro `python3.14`) | `/usr/local/bin/python`, `/usr/local/bin/python3` |
| pip | 26.2.2 | `/usr/local/bin/pip` |
| Node.js | v20.20.2 | `/usr/local/bin/node` |
| npm | 10.8.2 | `/usr/local/bin/npm` |
| Git | 2.53.0 | `/usr/bin/git` |
| SWI-Prolog | 9.2.9 *(installed during this session)* | `/usr/bin/swipl` |

Also present from the Debian package list: `build-essential`, `binutils` 2.46, `autoconf`, `automake`, `libtool`, `pkgconf`, `curl`, `wget`, `jq`, `ripgrep`, `rsync`, `socat`, `screen`, `sqlite3`, `xxd`, `openssh-client`/`openssh-server`, `bubblewrap`, and the `supabase` CLI. Ubuntu 26.04's Rust rewrites are also in place: `rust-coreutils` and `sudo-rs`.

Not found on `PATH`: `clang`, `clang++`, `cmake`, `ninja`, `gdb`, `lldb`, `java`, `rustc`, `cargo`, `go`, `docker`, `podman`.

The interpreter version check printed two versions, 3.14.8 and 3.14.4. The distro `python3.14` package is 3.14.4, so the `/usr/local` build that owns `pip` and the Python inventory below is the newer 3.14.8. Node is the older 20.x LTS line, even though everything else on the box is recent.

```text
gcc: /usr/bin/gcc
g++: /usr/bin/g++
clang: not found on PATH
clang++: not found on PATH
cmake: not found on PATH
make: /usr/bin/make
ninja: not found on PATH
gdb: not found on PATH
lldb: not found on PATH
python: /usr/local/bin/python
python3: /usr/local/bin/python3
pip: /usr/local/bin/pip
node: /usr/local/bin/node
npm: /usr/local/bin/npm
git: /usr/bin/git
swipl: /usr/bin/swipl
java: not found on PATH
rustc: not found on PATH
cargo: not found on PATH
go: not found on PATH
docker: not found on PATH
podman: not found on PATH
gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
GNU Make 4.4.1
Python 3.14.8
Python 3.14.4
pip 26.2.2 from /usr/local/lib/python3.14/site-packages/pip (python 3.14)
v20.20.2
10.8.2
git version 2.53.0
SWI-Prolog version 9.2.9 for x86_64-linux
```

## The desktop and computer-use stack

This is what makes the box a *computer* and not just a code interpreter. The image ships a complete headless X11 desktop:

| Component | Package / version |
|---|---|
| Virtual X server | `xvfb` 21.1.22 |
| Window manager | `openbox` 3.6.1 |
| Panel / settings | `xfce4-panel` 4.20.7, `xfconf`, `xsettingsd` |
| Terminal | `alacritty` 0.16.1 |
| X utilities | `x11-utils`, `x11-xserver-utils`, `x11-xkb-utils`, `xauth`, `xdg-utils` |
| GUI toolkit / accessibility | GTK 3.24.52, `at-spi2-core` 2.60.4, D-Bus 1.16.2 |
| Rendering | Mesa 26.0.8 (`libgallium`, software rendering since there is no GPU) |
| Office suite | LibreOffice 26.2.6 (Writer, Calc, Impress, Draw, Math, Base) + `python3-uno` |
| Fonts | DejaVu, Liberation, Noto (incl. CJK and color emoji), Roboto, Lato, Carlito/Caladea, URW base35, `ttf-mscorefonts-installer` |

No web browser package (Chromium, Firefox) is installed, so web browsing is presumably handled by a separate tool service rather than inside this VM. The UI automation helper (screenshots, input injection) is not visible as a Debian package either. It most likely talks to the X server directly, or runs over the vsock channel noted above.

Document, image, and media tooling:

| Software | Version |
|---|---|
| FFmpeg | 8.0.1 |
| ImageMagick | 7.1.2-18 (Q16) |
| libvips / `libvips-tools` | present (plus `pyvips` in Python) |
| Pandoc | 3.7.0.2 |
| Tesseract OCR | 5.5.0 (eng + osd) |
| Poppler utils | 26.01.0 |
| Ghostscript | 10.06.0 |
| qpdf | present |
| ExifTool | `libimage-exiftool-perl` |
| librsvg | present |

## Installed Python packages

145 distributions visible to the default Python. The interesting ones:

- **Perplexity internals:** `pplx_sdk`, `pplx-python-sdks-llm-api`, and three `idl-protobuf-perplexity-llm-api-*` packages (protobuf/gRPC stubs for Perplexity's internal LLM API). One of them is versioned `2026.10.22.1792629890+b7907f3`, a build stamped the day before capture, so the image is rebuilt frequently.
- **Third-party model SDKs:** `anthropic` 2.1.0 and `openai` 3.36.0.
- **Infrastructure:** `modal` 1.5.2 (Modal serverless compute client), `boto3`/`s3transfer`, `git-remote-s3`, `grpcio`/`grpclib`, `fastapi`/`uvicorn`/`Flask`.
- **Observability:** `ddtrace` 4.16.0, `ddtrace-internal`, `datadog`, `opentelemetry-api`.
- **Document conversion:** `markitdown`, `markdownify`, `pdf2docx`, `pymupdf`, `pdfplumber`, `pypdf`, `pypdfium2`, `python-docx`, `python-pptx`, `openpyxl`, `xlsxwriter`, `reportlab`, `fpdf2`, `mat2` (metadata scrubbing).
- **Media / vision:** `opencv-python-headless` 5.0, `onnxruntime`, `pillow` 13 + `pillow_heif`, `pyvips`, `pytesseract`, `yt-dlp`, `mutagen`, `magika` (Google's ML file-type detector).
- **Language detection:** `fast-langdetect`, `fasttext-predict-v2`, `hanzidentifier`, `zhon`.
- **Agent tooling:** `skills-ref` 0.1.1, a reference library for agent "skills" packages.

Notably absent: no PyTorch, TensorFlow, scikit-learn, or Jupyter. The numeric stack is just `numpy`, `pandas` 3.0, `scipy`, and `matplotlib`.

```text
Package                                                       Version
------------------------------------------------------------- -----------------------------
aiohappyeyeballs                                              2.7.1
aiohttp                                                       3.14.5
aiosignal                                                     1.4.0
annotated-doc                                                 0.0.5
annotated-types                                               0.8.0
anthropic                                                     2.1.0
anyio                                                         4.15.1
attrs                                                         26.1.0
beautifulsoup4                                                4.15.0
blinker                                                       1.9.0
boto3                                                         1.43.117
botocore                                                      1.43.117
bytecode                                                      0.19.1
cbor2                                                         6.1.5
certifi                                                       2026.10.19
cffi                                                          2.1.1
charset-normalizer                                            3.5.2
click                                                         8.5.0
colorlog                                                      6.12.0
contourpy                                                     1.4.0
cryptography                                                  50.0.2
cycler                                                        0.12.1
datadog                                                       0.51.0
ddtrace                                                       4.16.0
ddtrace-internal                                              0.1.0
defusedxml                                                    0.7.1
docstring_parser                                              0.18.0
envier                                                        0.6.1
et_xmlfile                                                    2.0.0
fast-langdetect                                               1.1.0
fastapi                                                       0.159.1
fasttext-predict-v2                                           1.1.0
fire                                                          0.7.1
Flask                                                         3.1.3
flatbuffers                                                   25.12.19
fonttools                                                     4.67.0
fpdf2                                                         2.8.9
frozenlist                                                    1.8.0
git-remote-s3                                                 0.4.2
grpcio                                                        1.80.0
grpclib                                                       0.4.9
h11                                                           0.16.0
h2                                                            4.4.1
hanzidentifier                                                1.3.0
hpack                                                         4.2.0
httpcore2                                                     2.16.0
httptools                                                     0.9.0
httpx2                                                        2.16.0
hyperframe                                                    6.1.0
idl-protobuf-perplexity-llm-api-common-llm-api-common-pyproto 2026.10.22.1792629890+b7907f3
idl-protobuf-perplexity-llm-api-llm-api-pygrpc                0.0.0+local
idl-protobuf-perplexity-llm-api-llm-api-pyproto               0.0.0+local
idna                                                          3.20
itsdangerous                                                  2.2.0
Jinja2                                                        3.1.6
jiter                                                         0.13.0
jmespath                                                      1.1.0
kiwisolver                                                    1.5.1
lxml                                                          6.1.3
lz4                                                           4.4.5
magika                                                        1.0.3
markdown-it-py                                                4.2.0
markdownify                                                   1.2.3
markitdown                                                    0.1.9
MarkupSafe                                                    3.0.4
mat2                                                          0.15.0
matplotlib                                                    3.11.2
mdurl                                                         0.1.2
modal                                                         1.5.2
multidict                                                     7.1.0
mutagen                                                       1.48.1
numpy                                                         2.5.4
onnxruntime                                                   1.31.0
openai                                                        3.36.0
opencv-python-headless                                        5.0.0.93
openpyxl                                                      3.1.5
opentelemetry-api                                             1.45.1
orjson                                                        3.11.8
packaging                                                     26.3
pandas                                                        3.0.6
pdf2docx                                                      0.5.13
pdf2image                                                     1.17.0
pdfminer.six                                                  20260107
pdfplumber                                                    0.11.10
pillow                                                        13.0.0
pillow_heif                                                   1.8.0
pip                                                           26.2.2
pplx-python-sdks-llm-api                                      0.0.0+local
pplx_sdk                                                      0.0.0+local
propcache                                                     0.5.4
protobuf                                                      7.35.1
pycairo                                                       1.29.2
pycparser                                                     3.11
pydantic                                                      2.12.5
pydantic_core                                                 2.41.5
Pygments                                                      2.21.0
PyGObject                                                     3.48.2
pymupdf                                                       1.28.2
pyparsing                                                     3.3.3
pypdf                                                         6.21.2
pypdfium2                                                     5.14.0
pytesseract                                                   0.3.13
python-dateutil                                               2.9.0.post0
python-docx                                                   1.2.0
python-dotenv                                                 1.2.4
python-pptx                                                   1.0.2
pytz                                                          2026.5
pyvips                                                        3.2.0
PyYAML                                                        6.0.3
reportlab                                                     5.0.1
requests                                                      2.34.2
rich                                                          15.0.0
robust-downloader                                             0.0.2
s3transfer                                                    0.19.3
scipy                                                         1.18.1
six                                                           1.17.0
skills-ref                                                    0.1.1
sniffio                                                       1.3.1
soupsieve                                                     3.0.4
sqlglot                                                       30.24.0
starlette                                                     1.9.0
strictyaml                                                    1.7.3
synchronicity                                                 0.12.6
tenacity                                                      9.1.2
termcolor                                                     3.3.0
toml                                                          0.10.2
tqdm                                                          4.70.1
truststore                                                    0.10.5
types-certifi                                                 2021.10.8.3
types-toml                                                    0.10.8.20260518
typing_extensions                                             4.16.0
typing-inspection                                             0.4.4
urllib3                                                       2.8.0
uuid7                                                         0.1.0
uvicorn                                                       0.54.0
uvloop                                                        0.23.0
watchfiles                                                    1.3.0
websockets                                                    17.3
Werkzeug                                                      3.1.9
wrapt                                                         2.5.1
xlrd                                                          2.0.2
xlsxwriter                                                    3.3.0
yarl                                                          1.25.1
yt-dlp                                                        2026.10.21
zhon                                                          2.1.1
```

## Global Node packages

```text
/usr/local/lib
+-- @anthropic-ai/claude-code@2.1.286
+-- @box/cli@4.10.1
+-- @googleworkspace/cli@0.22.5
+-- @openai/codex@0.130.0
+-- convex@1.42.3
+-- corepack@0.34.6
+-- npm@10.8.2
+-- serve@14.2.6
`-- vercel@50.28.0

```

The global npm prefix has **two third-party coding agents preinstalled**, `@anthropic-ai/claude-code` 2.1.286 and `@openai/codex` 0.130.0, plus CLIs for the services Perplexity Computer connects to: `vercel`, `convex`, `@box/cli`, and `@googleworkspace/cli`. `serve` is there for quick static hosting from the VM.

## Installed Debian package inventory

All 847 installed packages (`dpkg-query` name and version). The SWI-Prolog packages (`swi-prolog-core`, `swi-prolog-core-packages`, `swi-prolog-nox`) and their dependencies were installed during this session.

```text
3cpio	0.14.0-1ubuntu1
adduser	3.153ubuntu1
adwaita-icon-theme	50.0-1
alacritty	0.16.1-2ubuntu1
amd64-microcode	3.20251202.1ubuntu2
apache2-utils	2.4.66-2ubuntu2.6
apt	3.2.0
at-spi2-common	2.60.4-0ubuntu0.1
at-spi2-core	2.60.4-0ubuntu0.1
autoconf	2.72-3.1ubuntu2
automake	1:1.18.1-3build1
autopoint	0.23.2-1
autotools-dev	20240727.1build1
base-files	14ubuntu6.2
base-passwd	3.6.8
bash	5.3-2ubuntu1
bc	1.07.1-4build1
bind9-dnsutils	1:9.20.24-1ubuntu0.4
bind9-host	1:9.20.24-1ubuntu0.4
bind9-libs:amd64	1:9.20.24-1ubuntu0.4
binutils	2.46-3ubuntu2
binutils-common:amd64	2.46-3ubuntu2
binutils-x86-64-linux-gnu	2.46-3ubuntu2
bsdextrautils	2.41.3-3ubuntu2.2
bsdutils	1:2.41.3-3ubuntu2.2
bubblewrap	0.11.1-1ubuntu0.3
build-essential	12.12ubuntu2.26.04.2
bzip2	1.0.8-6ubuntu0.1
ca-certificates	20260601~26.04.1
cabextract	1.11-2build1
console-setup	1.237ubuntu3.1
console-setup-linux	1.237ubuntu3.1
coreutils	9.5-1ubuntu2+0.0.0~ubuntu25
coreutils-from-uutils	0.0.0~ubuntu25
cpp	4:15.2.0-5ubuntu1
cpp-15	15.2.0-16ubuntu1
cpp-15-x86-64-linux-gnu	15.2.0-16ubuntu1
cpp-x86-64-linux-gnu	4:15.2.0-5ubuntu1
curl	8.18.0-1ubuntu2.8
dash	0.5.12-12ubuntu3
dbus	1.16.2-2ubuntu4
dbus-bin	1.16.2-2ubuntu4
dbus-daemon	1.16.2-2ubuntu4
dbus-session-bus-common	1.16.2-2ubuntu4
dbus-system-bus-common	1.16.2-2ubuntu4
dbus-user-session	1.16.2-2ubuntu4
dconf-gsettings-backend:amd64	0.49.0-4
dconf-service	0.49.0-4
debconf	1.5.92
debhelper	13.31ubuntu1
debianutils	5.23.2build1
debugedit	1:5.3-4
desktop-file-utils	0.28-1build1
dh-autoreconf	21+nmu1
dh-strip-nondeterminism	1.15.0-1build1
diffutils	1:3.12-1ubuntu0.1
dirmngr	2.4.8-4ubuntu3.1
distro-info	1.15
distro-info-data	0.72-0ubuntu0.26.04.1
dmidecode	3.6-2build1
dmsetup	2:1.02.205-2ubuntu3
dpkg	1.23.7ubuntu1
dpkg-dev	1.23.7ubuntu1
dwz	0.16-4
e2fsprogs	1.47.2-3ubuntu4
exo-utils	4.20.0-1build1
falcon-sensor	7.38.0-19105
fdisk	2.41.3-3ubuntu2.2
ffmpeg	7:8.0.1-3ubuntu2
file	1:5.46-5build2
findutils	4.10.0-3build2
fontconfig	2.17.1-3ubuntu1
fontconfig-config	2.17.1-3ubuntu1
fonts-crosextra-caladea	20200211-2
fonts-crosextra-carlito	20230309-2
fonts-dejavu	2.37-8build1
fonts-dejavu-core	2.37-8build1
fonts-dejavu-extra	2.37-8build1
fonts-dejavu-mono	2.37-8build1
fonts-font-awesome	5.0.10+really4.7.0~dfsg-4.1build1
fonts-freefont-ttf	20211204+svn4273-4build1
fonts-lato	2.015-1build1
fonts-liberation	1:2.1.5-3build1
fonts-liberation-sans-narrow	1:1.07.6-4build1
fonts-linuxlibertine	5.3.0-6build1
fonts-noto-cjk	1:20240730+repack1-1build1
fonts-noto-color-emoji	2.051-1build1
fonts-noto-core	20201225-2build1
fonts-noto-mono	20201225-2build1
fonts-noto-ui-core	20201225-2build1
fonts-opensymbol	4:102.12+LibO26.2.6.3-0ubuntu0.26.04.2
fonts-roboto	2:0~20170802-6
fonts-roboto-unhinted	2:0~20170802-6
fonts-sil-gentium	20081126:1.03-4build1
fonts-sil-gentium-basic	1.102-1.1build1
fonts-tlwg-loma-otf	1:0.7.3-1build1
fonts-unifont	1:16.0.04-1build1
fonts-urw-base35	20200910-8build1
g++	4:15.2.0-5ubuntu1
g++-15	15.2.0-16ubuntu1
g++-15-x86-64-linux-gnu	15.2.0-16ubuntu1
g++-x86-64-linux-gnu	4:15.2.0-5ubuntu1
gcc	4:15.2.0-5ubuntu1
gcc-15	15.2.0-16ubuntu1
gcc-15-base:amd64	15.2.0-16ubuntu1
gcc-15-x86-64-linux-gnu	15.2.0-16ubuntu1
gcc-16-base:amd64	16-20260322-1ubuntu1
gcc-x86-64-linux-gnu	4:15.2.0-5ubuntu1
gettext	0.23.2-1
gettext-base	0.23.2-1
gfortran	4:15.2.0-5ubuntu1
gfortran-15	15.2.0-16ubuntu1
gfortran-15-x86-64-linux-gnu	15.2.0-16ubuntu1
gfortran-x86-64-linux-gnu	4:15.2.0-5ubuntu1
ghostscript	10.06.0~dfsg-3ubuntu1.2
gir1.2-freedesktop:amd64	1.86.0-6build1
gir1.2-gdkpixbuf-2.0:amd64	2.44.5+dfsg-4ubuntu1
gir1.2-girepository-2.0:amd64	1.86.0-6build1
gir1.2-girepository-3.0:amd64	2.88.0-1ubuntu0.1
gir1.2-glib-2.0:amd64	2.88.0-1ubuntu0.1
gir1.2-poppler-0.18:amd64	26.01.0-2ubuntu0.3
gir1.2-rsvg-2.0:amd64	2.61.3+dfsg-3ubuntu0.1
gir1.2-vips-8.0	8.18.0-1build1
git	1:2.53.0-1ubuntu1
git-lfs	3.7.1-1
git-man	1:2.53.0-1ubuntu1
glycin-loaders	2.1.5+ds-0ubuntu0.2
glycin-thumbnailers	2.1.5+ds-0ubuntu0.2
gnu-coreutils	9.7-3ubuntu2.1
gnupg	2.4.8-4ubuntu3.1
gpg	2.4.8-4ubuntu3.1
gpg-agent	2.4.8-4ubuntu3.1
gpgconf	2.4.8-4ubuntu3.1
gpgsm	2.4.8-4ubuntu3.1
gpgv	2.4.8-4ubuntu3.1
grep	3.12-1
groff-base	1.23.0-10
gsettings-desktop-schemas	50.0-1ubuntu2
gtk-update-icon-cache	4.22.4+ds-0ubuntu0.1
gzip	1.14-1~exp2ubuntu1.1
hicolor-icon-theme	0.18-2build1
hostname	3.25build1
imagemagick	8:7.1.2.18+dfsg1-1
imagemagick-7-common	8:7.1.2.18+dfsg1-1
imagemagick-7.q16	8:7.1.2.18+dfsg1-1
init-system-helpers	1.69
inotify-tools	4.25.9.0-1
intel-microcode	3.20260210.1ubuntu2
intltool-debian	0.35.0+20060710.6build1
iproute2	6.19.0-1ubuntu1.1
iputils-ping	3:20250605-1ubuntu1
iso-codes	4.20.1-1
iucode-tool	2.3.1-3build2
javascript-common	12+nmu1build1
jq	1.8.1-4ubuntu2
kbd	2.7.1-2ubuntu2
keyboard-configuration	1.237ubuntu3.1
kmod	34.2-2ubuntu2
libabsl20260107:amd64	20260107.0-4
libabw-0.1-1:amd64	0.1.3-1build6
libacl1:amd64	2.3.2-2
libaom3:amd64	3.13.1-2ubuntu0.1
libapparmor1:amd64	5.0.2-0ubuntu1~26.04.1
libapr1t64:amd64	1.7.6-3
libaprutil1t64:amd64	1.6.3-3ubuntu3.1
libapt-pkg7.0:amd64	3.2.0
libarchive-cpio-perl	0.10-3
libarchive-zip-perl	1.68-1
libarchive13t64:amd64	3.8.5-1ubuntu2.3
libargon2-1:amd64	0~20190702+dfsg-5
libasan8:amd64	16-20260322-1ubuntu1
libasound2-data	1.2.15.3-1ubuntu1.1
libasound2t64:amd64	1.2.15.3-1ubuntu1.1
libass9:amd64	1:0.17.4-2
libassuan9:amd64	3.0.2-2build1
libasyncns0:amd64	0.8-7
libatk-bridge2.0-0t64:amd64	2.60.4-0ubuntu0.1
libatk1.0-0t64:amd64	2.60.4-0ubuntu0.1
libatomic1:amd64	16-20260322-1ubuntu1
libatspi2.0-0t64:amd64	2.60.4-0ubuntu0.1
libattr1:amd64	1:2.5.2-4ubuntu0.1
libaudit-common	1:4.1.2-1ubuntu0.1
libaudit1:amd64	1:4.1.2-1ubuntu0.1
libavahi-client3:amd64	0.8-18ubuntu1.1
libavahi-common-data:amd64	0.8-18ubuntu1.1
libavahi-common3:amd64	0.8-18ubuntu1.1
libavc1394-0:amd64	0.5.4-5build4
libavcodec62:amd64	7:8.0.1-3ubuntu2
libavdevice62:amd64	7:8.0.1-3ubuntu2
libavfilter11:amd64	7:8.0.1-3ubuntu2
libavformat62:amd64	7:8.0.1-3ubuntu2
libavutil60:amd64	7:8.0.1-3ubuntu2
libbinutils:amd64	2.46-3ubuntu2
libblkid1:amd64	2.41.3-3ubuntu2.2
libbluray3:amd64	1:1.4.1-1
libboost-iostreams1.90.0:amd64	1.90.0-6ubuntu1
libboost-locale1.90.0:amd64	1.90.0-6ubuntu1
libboost-thread1.90.0:amd64	1.90.0-6ubuntu1
libbpf1:amd64	1:1.6.3-1ubuntu1
libbrotli1:amd64	1.2.0-3build1
libbs2b0:amd64	3.1.0+dfsg-8build1
libbsd0:amd64	0.12.2-2build2
libbz2-1.0:amd64	1.0.8-6ubuntu0.1
libc-bin	2.43-2ubuntu2.4
libc-dev-bin	2.43-2ubuntu2.4
libc-gconv-modules-extra:amd64	2.43-2ubuntu2.4
libc6:amd64	2.43-2ubuntu2.4
libc6-dev:amd64	2.43-2ubuntu2.4
libcairo-gobject2:amd64	1.18.4-3
libcairo2:amd64	1.18.4-3
libcap-ng0:amd64	0.8.5-4build5
libcap2:amd64	1:2.75-10ubuntu2
libcap2-bin	1:2.75-10ubuntu2
libcbor0.10:amd64	0.10.2-2ubuntu3
libcc1-0:amd64	16-20260322-1ubuntu1
libcdio-cdda2t64:amd64	10.2+2.0.2-2
libcdio-paranoia2t64:amd64	10.2+2.0.2-2
libcdio19t64:amd64	2.2.0-4build1
libcdr-0.1-1:amd64	0.1.7-1build4
libcfitsio10t64:amd64	4.6.3-1
libcgif0:amd64	0.5.1-1
libchromaprint1:amd64	1.6.0-2build1
libcjson1:amd64	1.7.19-2
libclucene-contribs1t64:amd64	2.3.3.4+dfsg-1.3
libclucene-core1t64:amd64	2.3.3.4+dfsg-1.3
libcodec2-1.2:amd64	1.2.0-4
libcolamd3:amd64	1:7.12.2+dfsg-1ubuntu1
libcolord2:amd64	1.4.8-3
libcom-err2:amd64	1.47.2-3ubuntu4
libcrypt-dev:amd64	1:4.5.1-1
libcrypt1:amd64	1:4.5.1-1
libctf-nobfd0:amd64	2.46-3ubuntu2
libctf0:amd64	2.46-3ubuntu2
libcups2t64:amd64	2.4.16-1ubuntu1.3
libcurl3t64-gnutls:amd64	8.18.0-1ubuntu2.8
libcurl4t64:amd64	8.18.0-1ubuntu2.8
libdatrie1:amd64	0.2.14-1
libdav1d7:amd64	1.5.3-1
libdb5.3t64:amd64	5.3.28+dfsg2-10ubuntu1
libdbus-1-3:amd64	1.16.2-2ubuntu4
libdbusmenu-glib4:amd64	18.10.20180917~bzr492+repack1-4build1
libdbusmenu-gtk3-4:amd64	18.10.20180917~bzr492+repack1-4build1
libdc1394-25:amd64	2.2.6-6
libdconf1:amd64	0.49.0-4
libde265-0:amd64	1.0.16-1build1
libdebconfclient0:amd64	0.280ubuntu1
libdebhelper-perl	13.31ubuntu1
libdecor-0-0:amd64	0.2.5-1
libdeflate0:amd64	1.23-2ubuntu1
libdevmapper1.02.1:amd64	2:1.02.205-2ubuntu3
libdisplay-info3:amd64	0.3.0-1
libdjvulibre-text	3.5.29-1
libdjvulibre21:amd64	3.5.29-1
libdpkg-perl	1.23.7ubuntu1
libdrm-amdgpu1:amd64	2.4.131-1
libdrm-common	2.4.131-1
libdrm-intel1:amd64	2.4.131-1
libdrm2:amd64	2.4.131-1
libdvdnav4:amd64	7.0.0-2
libdvdread8t64:amd64	7.0.1-1
libdw1t64:amd64	0.194-4
libe-book-0.1-1:amd64	0.1.3-2build9
libedit2:amd64	3.1-20251016-1
libefivar1t64:amd64	39-2
libelf1t64:amd64	0.194-4
libeot0:amd64	0.01-5build4
libepoxy0:amd64	1.5.10-2build1
libepubgen-0.1-1:amd64	0.1.1-1ubuntu8
liberror-perl	0.17030-1
libetonyek-0.1-1:amd64	0.1.13-2
libexif12:amd64	0.6.25-2ubuntu0.1
libexo-2-0:amd64	4.20.0-1build1
libexo-common	4.20.0-1build1
libexpat1:amd64	2.7.4-1ubuntu0.2
libext2fs2t64:amd64	1.47.2-3ubuntu4
libexttextcat-2.0-0:amd64	3.4.7-2
libexttextcat-data	3.4.7-2
libfdisk1:amd64	2.41.3-3ubuntu2.2
libffi8:amd64	3.5.2-4
libfftw3-double3:amd64	3.3.10-2fakesync1build3
libfido2-1:amd64	1.16.0-2build1
libfile-stripnondeterminism-perl	1.15.0-1build1
libflac14:amd64	1.5.0+ds-5
libflite1:amd64	2.2-7build1
libfontconfig1:amd64	2.17.1-3ubuntu1
libfontenc1:amd64	1:1.1.8-1build2
libfreehand-0.1-1	0.1.2-3build4
libfreetype6:amd64	2.14.2+dfsg-1ubuntu0.2
libfribidi0:amd64	1.0.16-5
libgarcon-1-0:amd64	4.20.0-1build1
libgarcon-common	4.20.0-1build1
libgarcon-gtk3-1-0:amd64	4.20.0-1build1
libgbm1:amd64	26.0.8-1ubuntu0.3
libgcc-15-dev:amd64	15.2.0-16ubuntu1
libgcc-s1:amd64	16-20260322-1ubuntu1
libgcrypt20:amd64	1.12.0-2ubuntu1.1
libgdbm-compat4t64:amd64	1.26-1build1
libgdbm6t64:amd64	1.26-1build1
libgdk-pixbuf-2.0-0:amd64	2.44.5+dfsg-4ubuntu1
libgdk-pixbuf2.0-common	2.44.5+dfsg-4ubuntu1
libgfortran-15-dev:amd64	15.2.0-16ubuntu1
libgfortran5:amd64	16-20260322-1ubuntu1
libgif7:amd64	5.2.2-1ubuntu3.2
libgirepository-1.0-1:amd64	1.86.0-6build1
libgirepository-2.0-0:amd64	2.88.0-1ubuntu0.1
libgl1:amd64	1.7.0-3
libgl1-mesa-dri:amd64	26.0.8-1ubuntu0.3
libglib2.0-0t64:amd64	2.88.0-1ubuntu0.1
libglvnd0:amd64	1.7.0-3
libglx-mesa0:amd64	26.0.8-1ubuntu0.3
libglx0:amd64	1.7.0-3
libglycin-2-0:amd64	2.1.5+ds-0ubuntu0.2
libgme0:amd64	0.6.4-1
libgmp10:amd64	2:6.3.0+dfsg-5ubuntu2
libgnutls30t64:amd64	3.8.12-2ubuntu1.1
libgomp1:amd64	16-20260322-1ubuntu1
libgpg-error0:amd64	1.58-2
libgpgme45:amd64	2.0.1-2build1
libgpgmepp7:amd64	2.0.0-2
libgprofng0:amd64	2.46-3ubuntu2
libgraphite2-3:amd64	1.3.14-11ubuntu1.1
libgs-common	10.06.0~dfsg-3ubuntu1.2
libgs10:amd64	10.06.0~dfsg-3ubuntu1.2
libgs10-common	10.06.0~dfsg-3ubuntu1.2
libgsm1:amd64	1.0.23-2
libgssapi-krb5-2:amd64	1.22.1-2ubuntu4.1
libgstreamer-plugins-base1.0-0:amd64	1.28.2-1ubuntu0.1
libgstreamer1.0-0:amd64	1.28.2-1
libgtk-3-0t64:amd64	3.24.52-0ubuntu1
libgtk-3-common	3.24.52-0ubuntu1
libgtk-layer-shell0:amd64	0.10.0-1
libharfbuzz-icu0:amd64	12.3.2-2
libharfbuzz0b:amd64	12.3.2-2
libhdf5-310:amd64	1.14.6+repack-2
libheif-plugin-aomdec:amd64	1.21.2-3ubuntu0.6
libheif-plugin-aomenc:amd64	1.21.2-3ubuntu0.6
libheif-plugin-libde265:amd64	1.21.2-3ubuntu0.6
libheif-plugin-x265:amd64	1.21.2-3ubuntu0.6
libheif1:amd64	1.21.2-3ubuntu0.6
libhogweed6t64:amd64	3.10.2-1
libhunspell-1.7-0:amd64	1.7.2+really1.7.2-11
libhwasan0:amd64	16-20260322-1ubuntu1
libhwy1t64:amd64	1.3.0-2
libhyphen0:amd64	2.8.8-7build4
libice6:amd64	2:1.1.1-1build1
libicu78:amd64	78.2-2ubuntu1
libid3tag0:amd64	0.16.3-4
libidn12:amd64	1.43-2ubuntu0.26.04.1
libidn2-0:amd64	2.3.8-4build1
libiec61883-0:amd64	1.2.0-8
libijs-0.35:amd64	0.35-16
libimage-exiftool-perl	13.50+dfsg-1
libimagequant0:amd64	4.4.1-1
libimath-3-1-29t64:amd64	3.1.12-1ubuntu5
libimlib2t64:amd64	1.12.6-1
libinotifytools0:amd64	4.25.9.0-1
libisl23:amd64	0.27-1build1
libitm1:amd64	16-20260322-1ubuntu1
libjack-jackd2-0:amd64	1.9.22~dfsg-5build1
libjansson4:amd64	2.14-2build4
libjbig0:amd64	2.1-6.1ubuntu3
libjbig2dec0:amd64	0.20-1ubuntu0.26.04.1
libjemalloc2:amd64	5.3.0-4
libjpeg-turbo8:amd64	2.1.5-4ubuntu4
libjpeg8:amd64	8c-2ubuntu12
libjq1:amd64	1.8.1-4ubuntu2
libjs-jquery	3.7.1+dfsg+~3.5.33-1build1
libjs-sphinxdoc	8.2.3-12
libjson-c5:amd64	0.18+ds-3
libjxl0.11:amd64	0.11.1-6ubuntu4.2
libjxr-tools	1.2~git20170615.f752187-5.3build1
libjxr0t64:amd64	1.2~git20170615.f752187-5.3build1
libk5crypto3:amd64	1.22.1-2ubuntu4.1
libkeyutils1:amd64	1.6.3-6ubuntu3
libkmod2:amd64	34.2-2ubuntu2
libkrb5-3:amd64	1.22.1-2ubuntu4.1
libkrb5support0:amd64	1.22.1-2ubuntu4.1
libksba8:amd64	1.6.7-2build1
liblangtag-common	0.6.8-2
liblangtag1:amd64	0.6.8-2
liblcms2-2:amd64	2.17-1ubuntu0.2
libldap-common	2.6.10+dfsg-1ubuntu5
libldap2:amd64	2.6.10+dfsg-1ubuntu5
libleptonica6:amd64	1.86.0-1
liblerc4:amd64	4.0.0+ds-5ubuntu2
liblilv-0-0:amd64	0.26.2-1
libllvm21:amd64	1:21.1.8-6ubuntu1
liblmdb0:amd64	0.9.31-1build2
liblocale-gettext-perl	1.07-8
liblqr-1-0:amd64	0.4.2-2.2
liblsan0:amd64	16-20260322-1ubuntu1
liblsof0	4.99.4+dfsg-2build2
libltdl-dev:amd64	2.5.4-9
libltdl7:amd64	2.5.4-9
liblua5.4-0:amd64	5.4.8-1build1
liblz4-1:amd64	1.10.0-8
liblzma5:amd64	5.8.3-1
libmagic-mgc	1:5.46-5build2
libmagic1t64:amd64	1:5.46-5build2
libmagickcore-7.q16-10:amd64	8:7.1.2.18+dfsg1-1
libmagickcore-7.q16-10-extra:amd64	8:7.1.2.18+dfsg1-1
libmagickwand-7.q16-10:amd64	8:7.1.2.18+dfsg1-1
libmail-sendmail-perl	0.82-1build1
libmatio14:amd64	1.5.30-2
libmaxminddb0:amd64	1.12.2-1build2
libmbedcrypto16:amd64	3.6.5-0.1ubuntu2
libmd0:amd64	1.1.0-2build4
libmhash2:amd64	0.9.9.9-11
libmnl0:amd64	1.0.5-3build1
libmount1:amd64	2.41.3-3ubuntu2.2
libmp3lame0:amd64	3.101~svn6525+dfsg-2ubuntu0.1
libmpc3:amd64	1.3.1-3
libmpfr6:amd64	4.2.2-3
libmpg123-0t64:amd64	1.33.3-2
libmspack0t64:amd64	0.11-1.1build2
libmspub-0.1-1:amd64	0.1.4-4build1
libmwaw-0.3-3:amd64	0.3.22-2
libmysofa1:amd64	1.3.3+dfsg-1ubuntu2
libmythes-1.2-0:amd64	2:1.2.5-2build1
libncursesw6:amd64	6.6+20251231-1
libnetpbm11t64:amd64	2:11.10.02-1build1
libnettle8t64:amd64	3.10.2-1
libnghttp2-14:amd64	1.68.0-2ubuntu0.2
libnl-3-200:amd64	3.12.0-2
libnl-genl-3-200:amd64	3.12.0-2
libnorm1t64:amd64	1.5.9+dfsg-4
libnpth0t64:amd64	1.8-3build1
libnspr4:amd64	2:4.38.2-1ubuntu1
libnss3:amd64	2:3.120-1ubuntu2.2
libnss3-tools	2:3.120-1ubuntu2.2
libnuma1:amd64	2.0.19-1build1
libobrender32	3.6.1-12ubuntu3
libobt2:amd64	3.6.1-12ubuntu3
libodfgen-0.1-1:amd64	0.1.8-3build1
libogg0:amd64	1.3.6-2
libonig5:amd64	6.9.10-1build1
libopenal-data	1:1.25.1-2
libopenal1:amd64	1:1.25.1-2
libopenexr-3-1-30:amd64	3.1.13-2build1
libopenjp2-7:amd64	2.5.4-1ubuntu0.1
libopenmpt0t64:amd64	0.8.4-1
libopenslide0	3.4.1+dfsg-7build4
libopus0:amd64	1.6.1-1
liborc-0.4-0t64:amd64	1:0.4.42-2
liborcus-0.21-0:amd64	0.21.0-4
liborcus-parser-0.21-0:amd64	0.21.0-4
libossp-uuid16:amd64	1.6.6-1
libp11-kit0:amd64	0.26.2-2
libpagemaker-0.0-0:amd64	0.0.4-1build5
libpam-modules:amd64	1.7.0-5ubuntu3.2
libpam-modules-bin	1.7.0-5ubuntu3.2
libpam-runtime	1.7.0-5ubuntu3.2
libpam-systemd:amd64	259.5-0ubuntu3.4
libpam0g:amd64	1.7.0-5ubuntu3.2
libpango-1.0-0:amd64	1.57.0-1
libpangocairo-1.0-0:amd64	1.57.0-1
libpangoft2-1.0-0:amd64	1.57.0-1
libpangoxft-1.0-0:amd64	1.57.0-1
libpaper2:amd64	2.2.5-0.3maysync1
libparted2t64:amd64	3.6-6
libpci3:amd64	1:3.14.0-1build2
libpciaccess0:amd64	0.18.1-1ubuntu4.1
libpcre2-8-0:amd64	10.46-1build1
libperl5.40:amd64	5.40.1-7ubuntu0.3
libpgm-5.3-0t64:amd64	5.3.128~dfsg-2.1build2
libpipeline1:amd64	1.5.8-2
libpixman-1-0:amd64	0.46.4-1
libpkgconf7:amd64	2.5.1-4
libplacebo360:amd64	7.360.0-3
libpng16-16t64:amd64	1.6.57-1ubuntu0.1
libpoppler-glib8t64:amd64	26.01.0-2ubuntu0.3
libpoppler156:amd64	26.01.0-2ubuntu0.3
libpopt0:amd64	1.19+dfsg-2build1
libproc2-0:amd64	2:4.0.4-9ubuntu1
libpsl5t64:amd64	0.21.2-1.1build2
libpulse0:amd64	1:17.0+dfsg1-2ubuntu4
libpython3-stdlib:amd64	3.14.3-0ubuntu2
libpython3.14:amd64	3.14.4-1ubuntu0.2
libpython3.14-minimal:amd64	3.14.4-1ubuntu0.2
libpython3.14-stdlib:amd64	3.14.4-1ubuntu0.2
libqpdf30:amd64	12.3.2-1
libquadmath0:amd64	16-20260322-1ubuntu1
librabbitmq4:amd64	0.15.0-1ubuntu0.26.04.2
libraptor2-0:amd64	2.0.16-6build1
librasqal3t64:amd64	0.9.33-3
librav1e0.8:amd64	0.8.1-7
libraw1394-11:amd64	2.1.2-2build4
libraw23t64:amd64	0.21.5b-1ubuntu1.1
librdf0t64:amd64	1.0.17-8
libreadline8t64:amd64	8.3-4
libreoffice-base-core	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-calc	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-common	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-core	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-draw	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-gtk3	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-impress	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-math	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-style-colibre	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-calc	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-common	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-draw	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-impress	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-math	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-uiconfig-writer	4:26.2.6.3-0ubuntu0.26.04.2
libreoffice-writer	4:26.2.6.3-0ubuntu0.26.04.2
librevenge-0.0-0:amd64	0.0.5-3build2
librist4:amd64	0.2.11+dfsg-1build1
librsvg2-2:amd64	2.61.3+dfsg-3ubuntu0.1
librtmp1:amd64	2.4+20151223.gitfa8646d.1-3
librubberband3:amd64	4.0.0+dfsg-2ubuntu1
libsamplerate0:amd64	0.2.2-4build2
libsasl2-2:amd64	2.1.28+dfsg1-9ubuntu3
libsasl2-modules-db:amd64	2.1.28+dfsg1-9ubuntu3
libsdl2-2.0-0:amd64	2.32.10+dfsg-6
libsdl2-classic:amd64	2.32.10+dfsg-6
libseccomp2:amd64	2.6.0-2ubuntu5
libselinux1:amd64	3.9-4build1
libsemanage-common	3.9-1build1
libsemanage2:amd64	3.9-1build1
libsensors-config	1:3.6.2-2build1
libsensors5:amd64	1:3.6.2-2build1
libsepol2:amd64	3.9-2
libserd-0-0:amd64	0.32.6-1
libsframe3:amd64	2.46-3ubuntu2
libsharpyuv0:amd64	1.5.0-0.1build1
libshine3:amd64	3.1.1-3build1
libsm6:amd64	2:1.2.6-1build1
libsmartcols1:amd64	2.41.3-3ubuntu2.2
libsnappy1v5:amd64	1.2.2-2
libsndfile1:amd64	1.2.2-4
libsodium23:amd64	1.0.18-2
libsord-0-0:amd64	0.16.20-1
libsoxr0:amd64	0.1.3-4.1
libspectre1:amd64	0.2.12-2
libspeex1:amd64	1.2.1-3build1
libsqlite3-0:amd64	3.46.1-9ubuntu0.3
libsratom-0-0:amd64	0.6.20-1
libsrt1.5-gnutls:amd64	1.5.4-3
libss2:amd64	1.47.2-3ubuntu4
libssh-4:amd64	0.11.3-1ubuntu2.1
libssh2-1t64:amd64	1.11.1-1ubuntu0.26.04.4
libssl3t64:amd64	3.5.5-1ubuntu3.7
libstartup-notification0:amd64	0.12-8build1
libstdc++-15-dev:amd64	15.2.0-16ubuntu1
libstdc++6:amd64	16-20260322-1ubuntu1
libsuitesparseconfig7:amd64	1:7.12.2+dfsg-1ubuntu1
libsvtav1enc2:amd64	2.3.0+dfsg-1build1
libswresample6:amd64	7:8.0.1-3ubuntu2
libswscale9:amd64	7:8.0.1-3ubuntu2
libsys-hostname-long-perl	1.5-3
libsystemd-shared:amd64	259.5-0ubuntu3.4
libsystemd0:amd64	259.5-0ubuntu3.4
libsz2:amd64	1.1.5-1
libtasn1-6:amd64	4.21.0-2
libtesseract5:amd64	5.5.0-1build1
libtext-charwidth-perl:amd64	0.04-11build4
libtext-wrapi18n-perl	0.06-10
libthai-data	0.1.30-1
libthai0:amd64	0.1.30-1
libtheoradec2:amd64	1.2.0+dfsg-6
libtheoraenc2:amd64	1.2.0+dfsg-6
libtiff6:amd64	4.7.0-3ubuntu5
libtinfo6:amd64	6.6+20251231-1
libtirpc-common	1.3.7-0.1
libtirpc3t64:amd64	1.3.7-0.1
libtool	2.5.4-9
libtsan2:amd64	16-20260322-1ubuntu1
libtwolame0:amd64	0.4.0-2build4
libubsan1:amd64	16-20260322-1ubuntu1
libuchardet0:amd64	0.0.8-2
libudev1:amd64	259.5-0ubuntu3.4
libudfread3:amd64	1.2.0-2
libunibreak6:amd64	6.1-3build1
libunistring5:amd64	1.3-2build1
libuno-cppu3t64	4:26.2.6.3-0ubuntu0.26.04.2
libuno-cppuhelpergcc3-3t64	4:26.2.6.3-0ubuntu0.26.04.2
libuno-purpenvhelpergcc3-3t64	4:26.2.6.3-0ubuntu0.26.04.2
libuno-sal3t64	4:26.2.6.3-0ubuntu0.26.04.2
libuno-salhelpergcc3-3t64	4:26.2.6.3-0ubuntu0.26.04.2
libunwind8:amd64	1.8.3-0ubuntu1
liburcu8t64:amd64	0.15.6-1
libusb-1.0-0:amd64	2:1.0.29-2build1
libuuid1:amd64	2.41.3-3ubuntu2.2
libuv1t64:amd64	1.51.0-2ubuntu1
libva-drm2:amd64	2.23.0-1ubuntu1
libva-x11-2:amd64	2.23.0-1ubuntu1
libva2:amd64	2.23.0-1ubuntu1
libvdpau1:amd64	1.5-4
libvidstab1.1:amd64	1.1.0-2.1
libvips-tools	8.18.0-1build1
libvips42t64:amd64	8.18.0-1build1
libvisio-0.1-1:amd64	0.1.10-1build1
libvorbis0a:amd64	1.3.7-3build2
libvorbisenc2:amd64	1.3.7-3build2
libvorbisfile3:amd64	1.3.7-3build2
libvpl2	1:2.16.0-1
libvpx12:amd64	1.16.0-3
libvulkan1:amd64	1.4.341.0-1
libwayland-client0:amd64	1.24.0-2
libwayland-cursor0:amd64	1.24.0-2
libwayland-egl1:amd64	1.24.0-2
libwebp7:amd64	1.5.0-0.1build1
libwebpdemux2:amd64	1.5.0-0.1build1
libwebpmux3:amd64	1.5.0-0.1build1
libwmflite-0.2-7:amd64	0.2.14-1
libwnck-3-0:amd64	43.3-1build1
libwnck-3-common	43.3-1build1
libwpd-0.10-10:amd64	0.10.3-2build3
libwpg-0.3-3:amd64	0.3.4-3build2
libwps-0.4-4:amd64	0.4.14-2build2
libwrap0:amd64	7.6.q-36build2
libx11-6:amd64	2:1.8.13-1ubuntu0.1
libx11-data	2:1.8.13-1ubuntu0.1
libx11-xcb1:amd64	2:1.8.13-1ubuntu0.1
libx264-165:amd64	2:0.165.3222+gitb35605ac-3build1
libx265-215:amd64	4.1-4
libxau6:amd64	1:1.0.11-1build2
libxaw7:amd64	2:1.0.16-1build1
libxcb-dri3-0:amd64	1.17.0-2ubuntu1
libxcb-glx0:amd64	1.17.0-2ubuntu1
libxcb-present0:amd64	1.17.0-2ubuntu1
libxcb-randr0:amd64	1.17.0-2ubuntu1
libxcb-render0:amd64	1.17.0-2ubuntu1
libxcb-shape0:amd64	1.17.0-2ubuntu1
libxcb-shm0:amd64	1.17.0-2ubuntu1
libxcb-sync1:amd64	1.17.0-2ubuntu1
libxcb-util1:amd64	0.4.1-1build1
libxcb-xfixes0:amd64	1.17.0-2ubuntu1
libxcb-xkb1:amd64	1.17.0-2ubuntu1
libxcb1:amd64	1.17.0-2ubuntu1
libxcomposite1:amd64	1:0.4.6-1build1
libxcursor1:amd64	1:1.2.3-1build1
libxdamage1:amd64	1:1.1.7-1
libxdmcp6:amd64	1:1.1.5-2
libxext6:amd64	2:1.3.4-1build3
libxfce4panel-2.0-4	4.20.7-1
libxfce4ui-2-0:amd64	4.20.2-1
libxfce4ui-common	4.20.2-1
libxfce4util-common	4.20.1-1build1
libxfce4util7:amd64	4.20.1-1build1
libxfce4windowing-0-0:amd64	4.20.5-1
libxfce4windowing-common	4.20.5-1
libxfconf-0-3:amd64	4.20.0-1build1
libxfixes3:amd64	1:6.0.0-2build2
libxfont2:amd64	1:2.0.6-2ubuntu0.2
libxft2:amd64	2.3.6-1build2
libxi6:amd64	2:1.8.2-2
libxinerama1:amd64	2:1.1.4-3build2
libxkbcommon-x11-0:amd64	1.13.1-1
libxkbcommon0:amd64	1.13.1-1
libxkbfile1:amd64	1:1.1.0-1build5
libxml2-16:amd64	2.15.2+dfsg-0.1ubuntu0.3
libxmlsec1-1:amd64	1.3.9-1
libxmlsec1-nss1:amd64	1.3.9-1
libxmu6:amd64	2:1.1.3-4
libxmuu1:amd64	2:1.1.3-4
libxpm4:amd64	1:3.5.17-1ubuntu0.26.04.2
libxrandr2:amd64	2:1.5.4-1build1
libxrender1:amd64	1:0.9.12-1build1
libxres1:amd64	2:1.2.1-1build2
libxshmfence1:amd64	1.3.3-1build1
libxslt1.1:amd64	1.1.45-0.1
libxss1:amd64	1:1.2.3-1build4
libxt6t64:amd64	1:1.2.1-1.3build1
libxtables12:amd64	1.8.11-2ubuntu3
libxtst6:amd64	2:1.2.5-1ubuntu0.1
libxv1:amd64	2:1.0.13-1
libxvidcore4:amd64	2:1.3.7-3
libxxf86dga1:amd64	2:1.1.5-1build2
libxxf86vm1:amd64	1:1.1.4-2
libxxhash0:amd64	0.8.3-2build1
libyajl2:amd64	2.1.0-5.1
libyaml-0-2:amd64	0.2.5-2build3
libzimg2:amd64	3.0.6+ds1-1
libzix-0-0:amd64	0.8.0-1
libzmq5:amd64	4.3.5-1build3
libzstd1:amd64	1.5.7+dfsg-3
libzvbi-common	0.2.44-1ubuntu2
libzvbi0t64:amd64	0.2.44-1ubuntu2
linux-base	4.15ubuntu5
linux-libc-dev:amd64	7.0.0-38.38
login	1:4.16.0-2+really2.41.3-3ubuntu2.2
login.defs	1:4.17.4-2ubuntu3
logsave	1.47.2-3ubuntu4
lsb-release	12.1-2build1
lsof	4.99.4+dfsg-2build2
lto-disabled-list	79
lxd-agent-loader	0.13ubuntu0
lxd-installer	14ubuntu0
m4	1.4.21-1
make	4.4.1-3
man-db	2.13.1-1build1
mawk	1.3.4.20260129-1
media-types	14.0.0build1
mesa-libgallium:amd64	26.0.8-1ubuntu0.3
microcode-initrd	4ubuntu
mokutil	0.7.2-2
mount	2.41.3-3ubuntu2.2
ncurses-base	6.6+20251231-1
ncurses-bin	6.6+20251231-1
ncurses-term	6.6+20251231-1
netbase	6.5build1
netpbm	2:11.10.02-1build1
ocl-icd-libopencl1:amd64	2.3.4-1
openbox	3.6.1-12ubuntu3
openssh-client	1:10.2p1-2ubuntu3.7
openssh-server	1:10.2p1-2ubuntu3.7
openssh-sftp-server	1:10.2p1-2ubuntu3.7
openssl	3.5.5-1ubuntu3.7
openssl-provider-legacy	3.5.5-1ubuntu3.7
pandoc	3.7.0.2+ds-1
pandoc-data	3.7.0.2-1build1
parted	3.6-6
passwd	1:4.17.4-2ubuntu3
patch	2.8-2build1
pci.ids	0.0~2026.02.12-1
pciutils	1:3.14.0-1build2
perl	5.40.1-7ubuntu0.3
perl-base	5.40.1-7ubuntu0.3
perl-modules-5.40	5.40.1-7ubuntu0.3
pinentry-curses	1.3.2-3ubuntu1
pkg-config:amd64	2.5.1-4
pkgconf:amd64	2.5.1-4
pkgconf-bin	2.5.1-4
po-debconf	1.0.22
poppler-data	0.4.12-1build1
poppler-utils	26.01.0-2ubuntu0.3
procps	2:4.0.4-9ubuntu1
python-apt-common	3.1.0ubuntu1.1
python-is-python3	3.13.3-1+build1
python3	3.14.3-0ubuntu2
python3-apt	3.1.0ubuntu1.1
python3-autocommand	2.2.2-4
python3-bcrypt	5.0.0-3build1
python3-blinker	1.9.0-2build1
python3-cffi-backend:amd64	2.0.0-3build1
python3-click	8.2.0+0.really.8.1.8-1build1
python3-cryptography	46.0.5-1ubuntu2
python3-dbus	1.4.0-1build2
python3-debconf	1.5.92
python3-debian	1.0.1ubuntu2
python3-distro	1.9.0-1build1
python3-distro-info	1.15
python3-distupgrade	1:26.04.27
python3-gi	3.56.2-1
python3-httplib2	0.22.0-1ubuntu0.1
python3-inflect	7.5.0-1build1
python3-jaraco.context	6.0.1-2
python3-jaraco.functools	4.1.0-1build1
python3-jaraco.text	4.0.0-1build1
python3-jwt	2.10.1-4ubuntu1
python3-launchpadlib	2.1.0-1build1
python3-lazr.restfulclient	0.14.6-3build1
python3-lazr.uri	1.0.6-7build1
python3-minimal	3.14.3-0ubuntu2
python3-more-itertools	10.8.0-1build1
python3-mutagen	1.47.0-1build1
python3-oauthlib	3.3.1-1build1
python3-packaging	26.0-1
python3-pip	25.1.1+dfsg-1ubuntu2
python3-pip-whl	25.1.1+dfsg-1ubuntu2
python3-pkg-resources	78.1.1-0.1build1
python3-pyparsing	3.3.2-2
python3-setuptools	78.1.1-0.1build1
python3-setuptools-whl	78.1.1-0.1build1
python3-typeguard	4.4.4-2
python3-typing-extensions	4.15.0-2
python3-uno	4:26.2.6.3-0ubuntu0.26.04.2
python3-update-manager	1:26.04.5
python3-venv	3.14.3-0ubuntu2
python3-wadllib	2.0.0-3
python3-wheel	0.46.3-2
python3-xkit	0.5.0ubuntu8
python3-yaml	6.0.3-1build1
python3-zipp	3.23.0-1build1
python3.14	3.14.4-1ubuntu0.2
python3.14-minimal	3.14.4-1ubuntu0.2
python3.14-venv	3.14.4-1ubuntu0.2
qpdf	12.3.2-1
readline-common	8.3-4
ripgrep	15.1.0-1ubuntu1
rpcsvc-proto	1.4.3-1build1
rsync	3.4.1+ds1-7ubuntu0.3
rust-coreutils	0.8.0-0ubuntu3
sbsigntool	0.9.4-3.1ubuntu9
screen	4.9.1-3ubuntu2
secureboot-db	1.9build2
sed	4.9-2ubuntu1
sensible-utils	0.0.26build1
shared-mime-info	2.4-5build3
socat	1.8.1.1-1ubuntu0.1
sqlite3	3.46.1-9ubuntu0.3
ssh-import-id	5.11-0ubuntu4
sudo	1.9.17p2-1ubuntu3.2
sudo-common	1.2ubuntu
sudo-rs	0.2.13-0ubuntu1.2
supabase	2.78.1
swi-prolog-core	9.2.9+dfsg-1.1build1
swi-prolog-core-packages	9.2.9+dfsg-1.1build1
swi-prolog-nox	9.2.9+dfsg-1.1build1
systemd	259.5-0ubuntu3.4
systemd-resolved	259.5-0ubuntu3.4
systemd-sysv	259.5-0ubuntu3.4
sysvinit-utils	3.15-5ubuntu1
tar	1.35+dfsg-4ubuntu0.4
tesseract-ocr	5.5.0-1build1
tesseract-ocr-eng	1:4.1.0-2build1
tesseract-ocr-osd	1:4.1.0-2build1
ttf-mscorefonts-installer	3.8.1ubuntu2
tzdata	2026c-0ubuntu0.26.04.1
ubuntu-drivers-common	1:0.10.9
ubuntu-keyring	2023.11.28.1build1
ubuntu-pro-client	38ubuntu0~26.04
ubuntu-release-upgrader-core	1:26.04.27
ucf	3.0052ubuntu1
udev	259.5-0ubuntu3.4
unminimize	0.5build1
uno-libs-private	4:26.2.6.3-0ubuntu0.26.04.2
update-manager-core	1:26.04.5
update-notifier-common	3.207.2
ure	4:26.2.6.3-0ubuntu0.26.04.2
usbutils	1:019-1
user-session-migration	0.5.1
util-linux	2.41.3-3ubuntu2.2
wget	1.25.0-2ubuntu4.4
x11-common	1:7.7+26ubuntu1
x11-utils	7.7+7build1
x11-xkb-utils	7.7+9build1
x11-xserver-utils	7.7+11build1
xauth	1:1.1.2-1.1build1
xdg-user-dirs	0.19-1
xdg-utils	1.2.1-2ubuntu2
xfce4-panel	4.20.7-1
xfconf	4.20.0-1build1
xfonts-cyrillic	1:1.0.5+nmu1build1
xfonts-encodings	1:1.0.5-0ubuntu3
xfonts-scalable	1:1.0.3-1.3build1
xfonts-utils	1:7.7+7build1
xkb-data	2.46-2
xserver-common	2:21.1.22-1ubuntu1.3
xsettingsd	1.0.2-1build2
xvfb	2:21.1.22-1ubuntu1.3
xxd	2:9.1.2141-1ubuntu4.9
xz-utils	5.8.3-1
zip	3.0-15ubuntu3
zlib1g:amd64	1:1.3.dfsg+really1.3.1-1ubuntu3.1
```

## GCC C++ include search paths

```text
#include "..." search starts here:
#include <...> search starts here:
 /usr/include/c++/15
 /usr/include/x86_64-linux-gnu/c++/15
 /usr/include/c++/15/backward
 /usr/lib/gcc/x86_64-linux-gnu/15/include
 /usr/local/include
 /usr/include/x86_64-linux-gnu
 /usr/include
End of search list.
```

## Header inventory

There are **5,192 header files** under `/usr/include`, `/usr/local/include`, and the GCC internal include directory. They are individual files, not packages. Nearly all of them come from a few development packages already listed above, plus the headers bundled with the `/usr/local` Node and Python builds:

| Location | Files | Comes from |
|---|---:|---|
| `/usr/local/include/node` | 2,365 | Node.js 20 install (V8, libuv, OpenSSL, N-API headers), not dpkg |
| `/usr/include/linux`, `asm-generic` | 851 | `linux-libc-dev` (kernel userspace API, not a build tree for the running 6.1 kernel) |
| `/usr/include/c++/15` | 811 | `libstdc++-15-dev` |
| `/usr/include/x86_64-linux-gnu` | 418 | `libc6-dev`, `libstdc++-15-dev` (arch-specific bits) |
| `/usr/include` (other top-level) | 308 | mostly `libc6-dev` (glibc), plus the smaller `linux-libc-dev` dirs (`drm`, `rdma`, `sound`, `scsi`, …), `libcrypt-dev`, and `libltdl-dev` |
| `/usr/local/include/python3.14` | 284 | the `/usr/local` Python 3.14.8 build |
| `/usr/lib/gcc/x86_64-linux-gnu/15/include` | 155 | `gcc-15` / `libgcc-15-dev` (intrinsics such as `immintrin.h`) |

The practical takeaway is what's **missing**: no third-party library development headers are installed. There is no `zlib.h`, no OpenSSL, curl, libpng/jpeg, SQLite, libffi, ncurses, or readline headers in `/usr/include`. Plain C/C++ against libc and libstdc++ builds out of the box. Anything that links a system library needs a `sudo apt install lib…-dev` first. The counts are based on filenames, not on compile or link tests.

## Visibility and caveats

- Everything above is a **point-in-time reading** from one session on 2026-10-23. The image is rebuilt often (see the Python protobuf build stamp), so versions will drift.
- The inventory is **not pristine**: SWI-Prolog and its dependencies were added during the session.
- Device nodes and installed packages show what is *present*, not what is attached or running. GPU absence is based on there being no GPU device nodes and no PCI devices at all.
- The host machine, the inference stack, and any external tool services (such as web browsing) are not observable from inside the guest.
- No environment-variable values, credentials, network addresses, or machine identifiers were collected.
