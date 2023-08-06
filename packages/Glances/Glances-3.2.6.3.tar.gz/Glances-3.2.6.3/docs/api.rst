.. _api:

API (Restfull/JSON) documentation
=================================

The Glances Restfull/API server could be ran using the following command line:

.. code-block:: bash

    # glances -w --disable-webui

Note: Change request URL api/3 by api/2 if you use Glances 2.x.

GET API status
--------------

This entry point should be used to check the API status.
It will return nothing but a 200 return code if everythin is OK.

Get the Rest API status::

    # curl -I http://localhost:61208/api/3/status
    "HTTP/1.0 200 OK"

GET plugins list
----------------

Get the plugins list::

    # curl http://localhost:61208/api/3/pluginslist
    ["alert",
     "amps",
     "cloud",
     "connections",
     "core",
     "cpu",
     "diskio",
     "docker",
     "folders",
     "fs",
     "gpu",
     "help",
     "ip",
     "irq",
     "load",
     "mem",
     "memswap",
     "network",
     "now",
     "percpu",
     "ports",
     "processcount",
     "processlist",
     "psutilversion",
     "quicklook",
     "raid",
     "sensors",
     "smart",
     "system",
     "uptime",
     "wifi"]

GET alert
---------

Get plugin stats::

    # curl http://localhost:61208/api/3/alert
    [[1653511582.0,
      -1,
      "WARNING",
      "MEM",
      81.37629268155027,
      81.37629268155027,
      81.37629268155027,
      81.37629268155027,
      1,
      [],
      "",
      "memory_percent"]]

GET amps
--------

Get plugin stats::

    # curl http://localhost:61208/api/3/amps
    [{"count": 0,
      "countmax": None,
      "countmin": 1.0,
      "key": "name",
      "name": "Dropbox",
      "refresh": 3.0,
      "regex": True,
      "result": None,
      "timer": 1.2215237617492676},
     {"count": 0,
      "countmax": 20.0,
      "countmin": None,
      "key": "name",
      "name": "Python",
      "refresh": 3.0,
      "regex": True,
      "result": None,
      "timer": 1.2214140892028809}]

Get a specific field::

    # curl http://localhost:61208/api/3/amps/name
    {"name": ["Dropbox", "Python", "Conntrack", "Nginx", "Systemd", "SystemV"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/amps/name/Dropbox
    {"Dropbox": [{"count": 0,
                  "countmax": None,
                  "countmin": 1.0,
                  "key": "name",
                  "name": "Dropbox",
                  "refresh": 3.0,
                  "regex": True,
                  "result": None,
                  "timer": 1.2215237617492676}]}

GET core
--------

Get plugin stats::

    # curl http://localhost:61208/api/3/core
    {"log": 4, "phys": 2}

Fields descriptions:

* **phys**: Number of physical cores (hyper thread CPUs are excluded) (unit is *number*)
* **log**: Number of logical CPUs. A logical CPU is the number of physical cores multiplied by the number of threads that can run on each core (unit is *number*)

Get a specific field::

    # curl http://localhost:61208/api/3/core/phys
    {"phys": 2}

GET cpu
-------

Get plugin stats::

    # curl http://localhost:61208/api/3/cpu
    {"cpucore": 4,
     "ctx_switches": 0,
     "guest": 0.0,
     "guest_nice": 0.0,
     "idle": 68.6,
     "interrupts": 0,
     "iowait": 0.1,
     "irq": 0.0,
     "nice": 0.0,
     "soft_interrupts": 0,
     "softirq": 0.0,
     "steal": 0.0,
     "syscalls": 0,
     "system": 4.3,
     "time_since_update": 1,
     "total": 35.6,
     "user": 27.0}

Fields descriptions:

* **total**: Sum of all CPU percentages (except idle) (unit is *percent*)
* **system**: percent time spent in kernel space. System CPU time is the time spent running code in the Operating System kernel (unit is *percent*)
* **user**: CPU percent time spent in user space. User CPU time is the time spent on the processor running your program's code (or code in libraries) (unit is *percent*)
* **iowait**: *(Linux)*: percent time spent by the CPU waiting for I/O operations to complete (unit is *percent*)
* **idle**: percent of CPU used by any program. Every program or task that runs on a computer system occupies a certain amount of processing time on the CPU. If the CPU has completed all tasks it is idle (unit is *percent*)
* **irq**: *(Linux and BSD)*: percent time spent servicing/handling hardware/software interrupts. Time servicing interrupts (hardware + software) (unit is *percent*)
* **nice**: *(Unix)*: percent time occupied by user level processes with a positive nice value. The time the CPU has spent running users' processes that have been *niced* (unit is *percent*)
* **steal**: *(Linux)*: percentage of time a virtual CPU waits for a real CPU while the hypervisor is servicing another virtual processor (unit is *percent*)
* **ctx_switches**: number of context switches (voluntary + involuntary) per second. A context switch is a procedure that a computer's CPU (central processing unit) follows to change from one task (or process) to another while ensuring that the tasks do not conflict (unit is *number*)
* **interrupts**: number of interrupts per second (unit is *number*)
* **soft_interrupts**: number of software interrupts per second. Always set to 0 on Windows and SunOS (unit is *number*)
* **syscalls**: number of system calls per second. Always 0 on Linux OS (unit is *number*)
* **cpucore**: Total number of CPU core (unit is *number*)
* **time_since_update**: Number of seconds since last update (unit is *seconds*)

Get a specific field::

    # curl http://localhost:61208/api/3/cpu/total
    {"total": 35.6}

GET diskio
----------

Get plugin stats::

    # curl http://localhost:61208/api/3/diskio
    [{"disk_name": "sda",
      "key": "disk_name",
      "read_bytes": 0,
      "read_count": 0,
      "time_since_update": 1,
      "write_bytes": 0,
      "write_count": 0},
     {"disk_name": "sda1",
      "key": "disk_name",
      "read_bytes": 0,
      "read_count": 0,
      "time_since_update": 1,
      "write_bytes": 0,
      "write_count": 0}]

Get a specific field::

    # curl http://localhost:61208/api/3/diskio/disk_name
    {"disk_name": ["sda", "sda1", "sda2", "sda5", "dm-0", "dm-1"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/diskio/disk_name/sda
    {"sda": [{"disk_name": "sda",
              "key": "disk_name",
              "read_bytes": 0,
              "read_count": 0,
              "time_since_update": 1,
              "write_bytes": 0,
              "write_count": 0}]}

GET docker
----------

Get plugin stats::

    # curl http://localhost:61208/api/3/docker
    [{"Command": ["/entrypoint.sh", "telegraf"],
      "Id": "9230f84acadbb7bc8c087d0827389c9a87bb7c7022a1a299dcf4a5f3a441f1d3",
      "Image": ["telegraf:latest"],
      "Names": ["telegraf"],
      "Status": "running",
      "Uptime": "1 weeks",
      "cpu_percent": 0.0,
      "io_r": None,
      "io_w": None,
      "key": "name",
      "memory_usage": 35647488,
      "name": "telegraf",
      "network_rx": None,
      "network_tx": None},
     {"Command": ["/run.sh"],
      "Id": "09d96704c3e6b6cb21657d990e3c8ae1e44bac779ded141efb8fed899563dd66",
      "Image": ["grafana/grafana:latest"],
      "Names": ["grafana"],
      "Status": "running",
      "Uptime": "1 weeks",
      "cpu_percent": 0.0,
      "io_r": None,
      "io_w": None,
      "key": "name",
      "memory_usage": None,
      "name": "grafana",
      "network_rx": None,
      "network_tx": None}]

GET fs
------

Get plugin stats::

    # curl http://localhost:61208/api/3/fs
    [{"device_name": "/dev/mapper/ubuntu--gnome--vg-root",
      "free": 99862933504,
      "fs_type": "ext4",
      "key": "mnt_point",
      "mnt_point": "/",
      "percent": 56.8,
      "size": 243396149248,
      "used": 131145760768}]

Get a specific field::

    # curl http://localhost:61208/api/3/fs/mnt_point
    {"mnt_point": ["/"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/fs/mnt_point//
    {"/": [{"device_name": "/dev/mapper/ubuntu--gnome--vg-root",
            "free": 99862933504,
            "fs_type": "ext4",
            "key": "mnt_point",
            "mnt_point": "/",
            "percent": 56.8,
            "size": 243396149248,
            "used": 131145760768}]}

GET ip
------

Get plugin stats::

    # curl http://localhost:61208/api/3/ip
    {"address": "192.168.0.33",
     "gateway": "192.168.0.254",
     "mask": "255.255.255.0",
     "mask_cidr": 24,
     "public_address": "91.166.228.228"}

Get a specific field::

    # curl http://localhost:61208/api/3/ip/address
    {"address": "192.168.0.33"}

GET load
--------

Get plugin stats::

    # curl http://localhost:61208/api/3/load
    {"cpucore": 4, "min1": 1.7607421875, "min15": 0.787109375, "min5": 1.0986328125}

Fields descriptions:

* **min1**: Average sum of the number of processes waiting in the run-queue plus the number currently executing over 1 minute (unit is *float*)
* **min5**: Average sum of the number of processes waiting in the run-queue plus the number currently executing over 5 minutes (unit is *float*)
* **min15**: Average sum of the number of processes waiting in the run-queue plus the number currently executing over 15 minutes (unit is *float*)
* **cpucore**: Total number of CPU core (unit is *number*)

Get a specific field::

    # curl http://localhost:61208/api/3/load/min1
    {"min1": 1.7607421875}

GET mem
-------

Get plugin stats::

    # curl http://localhost:61208/api/3/mem
    {"active": 2994515968,
     "available": 1459716096,
     "buffers": 120791040,
     "cached": 2113867776,
     "free": 1459716096,
     "inactive": 3645423616,
     "percent": 81.4,
     "shared": 646406144,
     "total": 7837945856,
     "used": 6378229760}

Fields descriptions:

* **total**: Total physical memory available (unit is *bytes*)
* **available**: The actual amount of available memory that can be given instantly to processes that request more memory in bytes; this is calculated by summing different memory values depending on the platform (e.g. free + buffers + cached on Linux) and it is supposed to be used to monitor actual memory usage in a cross platform fashion (unit is *bytes*)
* **percent**: The percentage usage calculated as (total - available) / total * 100 (unit is *percent*)
* **used**: Memory used, calculated differently depending on the platform and designed for informational purposes only (unit is *bytes*)
* **free**: Memory not being used at all (zeroed) that is readily available; note that this doesn't reflect the actual memory available (use 'available' instead) (unit is *bytes*)
* **active**: *(UNIX)*: memory currently in use or very recently used, and so it is in RAM (unit is *bytes*)
* **inactive**: *(UNIX)*: memory that is marked as not used (unit is *bytes*)
* **buffers**: *(Linux, BSD)*: cache for things like file system metadata (unit is *bytes*)
* **cached**: *(Linux, BSD)*: cache for various things (unit is *bytes*)
* **wired**: *(BSD, macOS)*: memory that is marked to always stay in RAM. It is never moved to disk (unit is *bytes*)
* **shared**: *(BSD)*: memory that may be simultaneously accessed by multiple processes (unit is *bytes*)

Get a specific field::

    # curl http://localhost:61208/api/3/mem/total
    {"total": 7837945856}

GET memswap
-----------

Get plugin stats::

    # curl http://localhost:61208/api/3/memswap
    {"free": 6304215040,
     "percent": 22.0,
     "sin": 1377947648,
     "sout": 3402825728,
     "time_since_update": 1,
     "total": 8082419712,
     "used": 1778204672}

Fields descriptions:

* **total**: Total swap memory (unit is *bytes*)
* **used**: Used swap memory (unit is *bytes*)
* **free**: Free swap memory (unit is *bytes*)
* **percent**: Used swap memory in percentage (unit is *percent*)
* **sin**: The number of bytes the system has swapped in from disk (cumulative) (unit is *bytes*)
* **sout**: The number of bytes the system has swapped out from disk (cumulative) (unit is *bytes*)
* **time_since_update**: Number of seconds since last update (unit is *seconds*)

Get a specific field::

    # curl http://localhost:61208/api/3/memswap/total
    {"total": 8082419712}

GET network
-----------

Get plugin stats::

    # curl http://localhost:61208/api/3/network
    [{"alias": None,
      "cumulative_cx": 473925792,
      "cumulative_rx": 236962896,
      "cumulative_tx": 236962896,
      "cx": 4156,
      "interface_name": "lo",
      "is_up": True,
      "key": "interface_name",
      "rx": 2078,
      "speed": 0,
      "time_since_update": 1,
      "tx": 2078},
     {"alias": None,
      "cumulative_cx": 5365392428,
      "cumulative_rx": 5016373584,
      "cumulative_tx": 349018844,
      "cx": 34101,
      "interface_name": "wlp2s0",
      "is_up": True,
      "key": "interface_name",
      "rx": 23539,
      "speed": 0,
      "time_since_update": 1,
      "tx": 10562}]

Fields descriptions:

* **interface_name**: Interface name (unit is *string*)
* **alias**: Interface alias name (optional) (unit is *string*)
* **rx**: The received/input rate (in bit per second) (unit is *bps*)
* **tx**: The sent/output rate (in bit per second) (unit is *bps*)
* **cumulative_rx**: The number of bytes received through the interface (cumulative) (unit is *bytes*)
* **cumulative_tx**: The number of bytes sent through the interface (cumulative) (unit is *bytes*)
* **speed**: Maximum interface speed (in bit per second). Can return 0 on some operating-system (unit is *bps*)
* **is_up**: Is the interface up ? (unit is *bool*)
* **time_since_update**: Number of seconds since last update (unit is *seconds*)

Get a specific field::

    # curl http://localhost:61208/api/3/network/interface_name
    {"interface_name": ["lo",
                        "wlp2s0",
                        "br-87386b77b676",
                        "br_grafana",
                        "docker0",
                        "br-119e6ee04e05",
                        "vethfbde85e",
                        "veth33a86dc",
                        "veth5ebe4bf",
                        "mpqemubr0"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/network/interface_name/lo
    {"lo": [{"alias": None,
             "cumulative_cx": 473925792,
             "cumulative_rx": 236962896,
             "cumulative_tx": 236962896,
             "cx": 4156,
             "interface_name": "lo",
             "is_up": True,
             "key": "interface_name",
             "rx": 2078,
             "speed": 0,
             "time_since_update": 1,
             "tx": 2078}]}

GET now
-------

Get plugin stats::

    # curl http://localhost:61208/api/3/now
    "2022-05-25 22:46:22 CEST"

GET percpu
----------

Get plugin stats::

    # curl http://localhost:61208/api/3/percpu
    [{"cpu_number": 0,
      "guest": 0.0,
      "guest_nice": 0.0,
      "idle": 56.9,
      "iowait": 0.0,
      "irq": 0.0,
      "key": "cpu_number",
      "nice": 0.0,
      "softirq": 0.0,
      "steal": 0.0,
      "system": 4.6,
      "total": 43.1,
      "user": 38.5},
     {"cpu_number": 1,
      "guest": 0.0,
      "guest_nice": 0.0,
      "idle": 73.8,
      "iowait": 0.0,
      "irq": 0.0,
      "key": "cpu_number",
      "nice": 0.0,
      "softirq": 0.0,
      "steal": 0.0,
      "system": 4.6,
      "total": 26.2,
      "user": 21.5}]

Get a specific field::

    # curl http://localhost:61208/api/3/percpu/cpu_number
    {"cpu_number": [0, 1, 2, 3]}

GET ports
---------

Get plugin stats::

    # curl http://localhost:61208/api/3/ports
    [{"description": "DefaultGateway",
      "host": "192.168.0.254",
      "indice": "port_0",
      "port": 0,
      "refresh": 30,
      "rtt_warning": None,
      "status": 0.011961,
      "timeout": 3}]

Get a specific field::

    # curl http://localhost:61208/api/3/ports/host
    {"host": ["192.168.0.254"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/ports/host/192.168.0.254
    {"192.168.0.254": [{"description": "DefaultGateway",
                        "host": "192.168.0.254",
                        "indice": "port_0",
                        "port": 0,
                        "refresh": 30,
                        "rtt_warning": None,
                        "status": 0.011961,
                        "timeout": 3}]}

GET processcount
----------------

Get plugin stats::

    # curl http://localhost:61208/api/3/processcount
    {"pid_max": 0, "running": 1, "sleeping": 269, "thread": 1530, "total": 335}

Get a specific field::

    # curl http://localhost:61208/api/3/processcount/total
    {"total": 335}

GET processlist
---------------

Get plugin stats::

    # curl http://localhost:61208/api/3/processlist
    [{"cmdline": ["/snap/firefox/1300/usr/lib/firefox/firefox"],
      "cpu_percent": 0.0,
      "cpu_times": pcputimes(user=7265.13, system=2644.4, children_user=4225.08, children_system=934.33, iowait=0.0),
      "gids": pgids(real=1000, effective=1000, saved=1000),
      "io_counters": [2597592064, 8660602880, 0, 0, 0],
      "key": "pid",
      "memory_info": pmem(rss=521797632, vms=14051770368, shared=142577664, text=643072, lib=0, data=1934319616, dirty=0),
      "memory_percent": 6.657326314656288,
      "name": "firefox",
      "nice": 0,
      "num_threads": 165,
      "pid": 10259,
      "ppid": 2922,
      "status": "S",
      "time_since_update": 1,
      "username": "nicolargo"},
     {"cmdline": ["/snap/firefox/1300/usr/lib/firefox/firefox",
                  "-contentproc",
                  "-childID",
                  "1",
                  "-isForBrowser",
                  "-prefsLen",
                  "628",
                  "-prefMapSize",
                  "267733",
                  "-jsInitLen",
                  "277212",
                  "-parentBuildID",
                  "20220502141216",
                  "-appDir",
                  "/snap/firefox/1300/usr/lib/firefox/browser",
                  "10259",
                  "true",
                  "tab"],
      "cpu_percent": 0.0,
      "cpu_times": pcputimes(user=1572.98, system=303.12, children_user=0.0, children_system=0.0, iowait=0.0),
      "gids": pgids(real=1000, effective=1000, saved=1000),
      "io_counters": [157250560, 0, 0, 0, 0],
      "key": "pid",
      "memory_info": pmem(rss=498479104, vms=3363688448, shared=77520896, text=643072, lib=0, data=767954944, dirty=0),
      "memory_percent": 6.359818161009762,
      "name": "WebExtensions",
      "nice": 0,
      "num_threads": 20,
      "pid": 10790,
      "ppid": 10259,
      "status": "S",
      "time_since_update": 1,
      "username": "nicolargo"}]

Get a specific field::

    # curl http://localhost:61208/api/3/processlist/pid
    {"pid": [10259,
             10790,
             271153,
             271200,
             10854,
             20979,
             10850,
             2922,
             21227,
             271409,
             21025,
             240874,
             62372,
             308697,
             10857,
             271083,
             271184,
             10814,
             308943,
             309130,
             306581,
             271118,
             12436,
             309195,
             306584,
             309267,
             271247,
             271208,
             3251,
             309448,
             337,
             2820,
             271397,
             52875,
             243846,
             2033,
             234429,
             271140,
             3279,
             138954,
             11390,
             265539,
             138989,
             138834,
             271089,
             266251,
             2505,
             3019,
             271088,
             1302,
             186877,
             2109,
             3161,
             186878,
             10597,
             2790,
             304566,
             3706,
             8716,
             20965,
             3347,
             3066,
             1133,
             2999,
             232395,
             3056,
             21229,
             3065,
             3206,
             8715,
             1601,
             1,
             2990,
             2964,
             3259,
             3227,
             3085,
             232398,
             2867,
             1150,
             3064,
             2073,
             3381,
             218290,
             1313,
             2900,
             2081,
             1990,
             20932,
             144959,
             1147,
             1176,
             3077,
             2769,
             3062,
             2781,
             3058,
             989,
             3178,
             20917,
             20916,
             3004,
             2933,
             271268,
             2831,
             3068,
             8959,
             1271,
             8941,
             10906,
             3034,
             241702,
             1173,
             2794,
             12458,
             1310,
             1132,
             2800,
             1115,
             2971,
             2798,
             1596,
             3268,
             1151,
             2960,
             3084,
             3136,
             3260,
             3129,
             3059,
             2923,
             2944,
             3232,
             3079,
             1139,
             1171,
             138811,
             3075,
             1167,
             3074,
             2977,
             3046,
             138968,
             2888,
             2949,
             3226,
             1161,
             24865,
             138923,
             3054,
             271091,
             2079,
             2828,
             990,
             2788,
             1127,
             2868,
             234438,
             1156,
             2805,
             2789,
             2080,
             2988,
             381,
             1123,
             1142,
             2931,
             2508,
             1429,
             1178,
             988,
             1130,
             21209,
             8757,
             266415,
             309432,
             997,
             1183,
             271104,
             996,
             1996,
             3274,
             1126,
             3528,
             138796,
             1116,
             138788,
             138767,
             138752,
             306441,
             138731,
             138901,
             309447,
             1914,
             138774,
             138745,
             2782,
             138724,
             3053,
             2012,
             2020,
             1997,
             1186,
             138894,
             2001,
             2,
             3,
             4,
             6,
             9,
             10,
             11,
             12,
             13,
             14,
             15,
             16,
             17,
             18,
             19,
             20,
             22,
             23,
             24,
             25,
             26,
             28,
             29,
             30,
             31,
             32,
             34,
             35,
             36,
             37,
             38,
             39,
             40,
             41,
             42,
             43,
             44,
             91,
             92,
             93,
             94,
             95,
             96,
             97,
             98,
             99,
             102,
             104,
             105,
             107,
             109,
             111,
             116,
             117,
             118,
             128,
             132,
             138,
             160,
             187,
             190,
             197,
             198,
             199,
             200,
             201,
             202,
             203,
             204,
             206,
             207,
             211,
             212,
             233,
             281,
             282,
             349,
             350,
             369,
             542,
             549,
             569,
             605,
             606,
             607,
             724,
             725,
             726,
             727,
             729,
             730,
             731,
             732,
             733,
             734,
             741,
             742,
             2039,
             2048,
             2049,
             2065,
             2066,
             2067,
             2068,
             2069,
             2070,
             2071,
             2072,
             2822,
             20919,
             20947,
             282038,
             303032,
             303046,
             304473,
             304481,
             304546,
             305737,
             305836,
             305906,
             305964,
             306989,
             307047,
             307166,
             307650,
             308467,
             308919,
             308920,
             308925,
             309347]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/processlist/pid/10259
    {"10259": [{"cmdline": ["/snap/firefox/1300/usr/lib/firefox/firefox"],
                "cpu_percent": 0.0,
                "cpu_times": [7265.13, 2644.4, 4225.08, 934.33, 0.0],
                "gids": [1000, 1000, 1000],
                "io_counters": [2597592064, 8660602880, 0, 0, 0],
                "key": "pid",
                "memory_info": [521797632,
                                14051770368,
                                142577664,
                                643072,
                                0,
                                1934319616,
                                0],
                "memory_percent": 6.657326314656288,
                "name": "firefox",
                "nice": 0,
                "num_threads": 165,
                "pid": 10259,
                "ppid": 2922,
                "status": "S",
                "time_since_update": 1,
                "username": "nicolargo"}]}

GET psutilversion
-----------------

Get plugin stats::

    # curl http://localhost:61208/api/3/psutilversion
    (5, 9, 0)

GET quicklook
-------------

Get plugin stats::

    # curl http://localhost:61208/api/3/quicklook
    {"cpu": 35.6,
     "cpu_hz": 3000000000.0,
     "cpu_hz_current": 2860000.0,
     "cpu_name": "Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz",
     "mem": 81.4,
     "percpu": [{"cpu_number": 0,
                 "guest": 0.0,
                 "guest_nice": 0.0,
                 "idle": 56.9,
                 "iowait": 0.0,
                 "irq": 0.0,
                 "key": "cpu_number",
                 "nice": 0.0,
                 "softirq": 0.0,
                 "steal": 0.0,
                 "system": 4.6,
                 "total": 43.1,
                 "user": 38.5},
                {"cpu_number": 1,
                 "guest": 0.0,
                 "guest_nice": 0.0,
                 "idle": 73.8,
                 "iowait": 0.0,
                 "irq": 0.0,
                 "key": "cpu_number",
                 "nice": 0.0,
                 "softirq": 0.0,
                 "steal": 0.0,
                 "system": 4.6,
                 "total": 26.2,
                 "user": 21.5},
                {"cpu_number": 2,
                 "guest": 0.0,
                 "guest_nice": 0.0,
                 "idle": 56.1,
                 "iowait": 0.8,
                 "irq": 0.0,
                 "key": "cpu_number",
                 "nice": 0.0,
                 "softirq": 0.0,
                 "steal": 0.0,
                 "system": 4.5,
                 "total": 43.9,
                 "user": 38.6},
                {"cpu_number": 3,
                 "guest": 0.0,
                 "guest_nice": 0.0,
                 "idle": 69.9,
                 "iowait": 0.0,
                 "irq": 0.0,
                 "key": "cpu_number",
                 "nice": 0.0,
                 "softirq": 0.0,
                 "steal": 0.0,
                 "system": 3.0,
                 "total": 30.1,
                 "user": 27.1}],
     "swap": 22.0}

Get a specific field::

    # curl http://localhost:61208/api/3/quicklook/cpu
    {"cpu": 35.6}

GET sensors
-----------

Get plugin stats::

    # curl http://localhost:61208/api/3/sensors
    [{"critical": 105,
      "key": "label",
      "label": "acpitz 1",
      "type": "temperature_core",
      "unit": "C",
      "value": 27,
      "warning": 105},
     {"critical": 105,
      "key": "label",
      "label": "acpitz 2",
      "type": "temperature_core",
      "unit": "C",
      "value": 29,
      "warning": 105}]

Get a specific field::

    # curl http://localhost:61208/api/3/sensors/label
    {"label": ["acpitz 1",
               "acpitz 2",
               "CPU",
               "Ambient",
               "SODIMM",
               "Package id 0",
               "Core 0",
               "Core 1",
               "BAT BAT0"]}

Get a specific item when field matchs the given value::

    # curl http://localhost:61208/api/3/sensors/label/acpitz 1
    {"acpitz 1": [{"critical": 105,
                   "key": "label",
                   "label": "acpitz 1",
                   "type": "temperature_core",
                   "unit": "C",
                   "value": 27,
                   "warning": 105}]}

GET system
----------

Get plugin stats::

    # curl http://localhost:61208/api/3/system
    {"hostname": "XPS13-9333",
     "hr_name": "Ubuntu 22.04 64bit",
     "linux_distro": "Ubuntu 22.04",
     "os_name": "Linux",
     "os_version": "5.15.0-27-generic",
     "platform": "64bit"}

Get a specific field::

    # curl http://localhost:61208/api/3/system/os_name
    {"os_name": "Linux"}

GET uptime
----------

Get plugin stats::

    # curl http://localhost:61208/api/3/uptime
    {"seconds": 1495537}

GET all stats
-------------

Get all Glances stats::

    # curl http://localhost:61208/api/3/all
    Return a very big dictionnary (avoid using this request, performances will be poor)...

GET stats history
-----------------

History of a plugin::

    # curl http://localhost:61208/api/3/cpu/history
    {"system": [["2022-05-25T22:46:23.083039", 4.3],
                ["2022-05-25T22:46:24.140665", 4.3],
                ["2022-05-25T22:46:25.239049", 5.5]],
     "user": [["2022-05-25T22:46:23.083029", 27.0],
              ["2022-05-25T22:46:24.140661", 27.0],
              ["2022-05-25T22:46:25.239044", 10.7]]}

Limit history to last 2 values::

    # curl http://localhost:61208/api/3/cpu/history/2
    {"system": [["2022-05-25T22:46:24.140665", 4.3],
                ["2022-05-25T22:46:25.239049", 5.5]],
     "user": [["2022-05-25T22:46:24.140661", 27.0],
              ["2022-05-25T22:46:25.239044", 10.7]]}

History for a specific field::

    # curl http://localhost:61208/api/3/cpu/system/history
    {"system": [["2022-05-25T22:46:23.083039", 4.3],
                ["2022-05-25T22:46:24.140665", 4.3],
                ["2022-05-25T22:46:25.239049", 5.5]]}

Limit history for a specific field to last 2 values::

    # curl http://localhost:61208/api/3/cpu/system/history
    {"system": [["2022-05-25T22:46:24.140665", 4.3],
                ["2022-05-25T22:46:25.239049", 5.5]]}

GET limits (used for thresholds)
--------------------------------

All limits/thresholds::

    # curl http://localhost:61208/api/3/all/limits
    {"alert": {"history_size": 3600.0},
     "amps": {"amps_disable": ["False"], "history_size": 3600.0},
     "cloud": {"history_size": 3600.0},
     "connections": {"connections_disable": ["True"],
                     "connections_nf_conntrack_percent_careful": 70.0,
                     "connections_nf_conntrack_percent_critical": 90.0,
                     "connections_nf_conntrack_percent_warning": 80.0,
                     "history_size": 3600.0},
     "core": {"history_size": 3600.0},
     "cpu": {"cpu_ctx_switches_careful": 160000.0,
             "cpu_ctx_switches_critical": 200000.0,
             "cpu_ctx_switches_warning": 180000.0,
             "cpu_disable": ["False"],
             "cpu_iowait_careful": 20.0,
             "cpu_iowait_critical": 25.0,
             "cpu_iowait_warning": 22.5,
             "cpu_steal_careful": 50.0,
             "cpu_steal_critical": 90.0,
             "cpu_steal_warning": 70.0,
             "cpu_system_careful": 50.0,
             "cpu_system_critical": 90.0,
             "cpu_system_log": ["False"],
             "cpu_system_warning": 70.0,
             "cpu_total_careful": 65.0,
             "cpu_total_critical": 85.0,
             "cpu_total_log": ["True"],
             "cpu_total_warning": 75.0,
             "cpu_user_careful": 50.0,
             "cpu_user_critical": 90.0,
             "cpu_user_log": ["False"],
             "cpu_user_warning": 70.0,
             "history_size": 3600.0},
     "diskio": {"diskio_disable": ["False"],
                "diskio_hide": ["loop.*", "/dev/loop*"],
                "history_size": 3600.0},
     "docker": {"docker_all": ["False"],
                "docker_disable": ["False"],
                "docker_max_name_size": 20.0,
                "history_size": 3600.0},
     "folders": {"folders_disable": ["False"], "history_size": 3600.0},
     "fs": {"fs_careful": 50.0,
            "fs_critical": 90.0,
            "fs_disable": ["False"],
            "fs_hide": ["/boot.*", "/snap.*"],
            "fs_warning": 70.0,
            "history_size": 3600.0},
     "gpu": {"gpu_disable": ["False"],
             "gpu_mem_careful": 50.0,
             "gpu_mem_critical": 90.0,
             "gpu_mem_warning": 70.0,
             "gpu_proc_careful": 50.0,
             "gpu_proc_critical": 90.0,
             "gpu_proc_warning": 70.0,
             "history_size": 3600.0},
     "help": {"history_size": 3600.0},
     "ip": {"history_size": 3600.0, "ip_disable": ["False"]},
     "irq": {"history_size": 3600.0, "irq_disable": ["True"]},
     "load": {"history_size": 3600.0,
              "load_careful": 0.7,
              "load_critical": 5.0,
              "load_disable": ["False"],
              "load_warning": 1.0},
     "mem": {"history_size": 3600.0,
             "mem_careful": 50.0,
             "mem_critical": 90.0,
             "mem_disable": ["False"],
             "mem_warning": 70.0},
     "memswap": {"history_size": 3600.0,
                 "memswap_careful": 50.0,
                 "memswap_critical": 90.0,
                 "memswap_disable": ["False"],
                 "memswap_warning": 70.0},
     "network": {"history_size": 3600.0,
                 "network_disable": ["False"],
                 "network_rx_careful": 70.0,
                 "network_rx_critical": 90.0,
                 "network_rx_warning": 80.0,
                 "network_tx_careful": 70.0,
                 "network_tx_critical": 90.0,
                 "network_tx_warning": 80.0},
     "now": {"history_size": 3600.0},
     "percpu": {"history_size": 3600.0,
                "percpu_disable": ["False"],
                "percpu_iowait_careful": 50.0,
                "percpu_iowait_critical": 90.0,
                "percpu_iowait_warning": 70.0,
                "percpu_system_careful": 50.0,
                "percpu_system_critical": 90.0,
                "percpu_system_warning": 70.0,
                "percpu_user_careful": 50.0,
                "percpu_user_critical": 90.0,
                "percpu_user_warning": 70.0},
     "ports": {"history_size": 3600.0,
               "ports_disable": ["False"],
               "ports_port_default_gateway": ["True"],
               "ports_refresh": 30.0,
               "ports_timeout": 3.0},
     "processcount": {"history_size": 3600.0, "processcount_disable": ["False"]},
     "processlist": {"history_size": 3600.0,
                     "processlist_cpu_careful": 50.0,
                     "processlist_cpu_critical": 90.0,
                     "processlist_cpu_warning": 70.0,
                     "processlist_disable": ["False"],
                     "processlist_mem_careful": 50.0,
                     "processlist_mem_critical": 90.0,
                     "processlist_mem_warning": 70.0,
                     "processlist_nice_warning": ["-20",
                                                  "-19",
                                                  "-18",
                                                  "-17",
                                                  "-16",
                                                  "-15",
                                                  "-14",
                                                  "-13",
                                                  "-12",
                                                  "-11",
                                                  "-10",
                                                  "-9",
                                                  "-8",
                                                  "-7",
                                                  "-6",
                                                  "-5",
                                                  "-4",
                                                  "-3",
                                                  "-2",
                                                  "-1",
                                                  "1",
                                                  "2",
                                                  "3",
                                                  "4",
                                                  "5",
                                                  "6",
                                                  "7",
                                                  "8",
                                                  "9",
                                                  "10",
                                                  "11",
                                                  "12",
                                                  "13",
                                                  "14",
                                                  "15",
                                                  "16",
                                                  "17",
                                                  "18",
                                                  "19"]},
     "psutilversion": {"history_size": 3600.0},
     "quicklook": {"history_size": 3600.0,
                   "quicklook_cpu_careful": 50.0,
                   "quicklook_cpu_critical": 90.0,
                   "quicklook_cpu_warning": 70.0,
                   "quicklook_disable": ["False"],
                   "quicklook_mem_careful": 50.0,
                   "quicklook_mem_critical": 90.0,
                   "quicklook_mem_warning": 70.0,
                   "quicklook_percentage_char": ["|"],
                   "quicklook_swap_careful": 50.0,
                   "quicklook_swap_critical": 90.0,
                   "quicklook_swap_warning": 70.0},
     "raid": {"history_size": 3600.0, "raid_disable": ["True"]},
     "sensors": {"history_size": 3600.0,
                 "sensors_battery_careful": 80.0,
                 "sensors_battery_critical": 95.0,
                 "sensors_battery_warning": 90.0,
                 "sensors_disable": ["False"],
                 "sensors_refresh": 4.0,
                 "sensors_temperature_core_careful": 60.0,
                 "sensors_temperature_core_critical": 80.0,
                 "sensors_temperature_core_warning": 70.0,
                 "sensors_temperature_hdd_careful": 45.0,
                 "sensors_temperature_hdd_critical": 60.0,
                 "sensors_temperature_hdd_warning": 52.0},
     "smart": {"history_size": 3600.0, "smart_disable": ["True"]},
     "system": {"history_size": 3600.0,
                "system_disable": ["False"],
                "system_refresh": 60},
     "uptime": {"history_size": 3600.0},
     "wifi": {"history_size": 3600.0,
              "wifi_careful": -65.0,
              "wifi_critical": -85.0,
              "wifi_disable": ["True"],
              "wifi_hide": ["lo", "docker.*"],
              "wifi_warning": -75.0}}

Limits/thresholds for the cpu plugin::

    # curl http://localhost:61208/api/3/cpu/limits
    {"cpu_ctx_switches_careful": 160000.0,
     "cpu_ctx_switches_critical": 200000.0,
     "cpu_ctx_switches_warning": 180000.0,
     "cpu_disable": ["False"],
     "cpu_iowait_careful": 20.0,
     "cpu_iowait_critical": 25.0,
     "cpu_iowait_warning": 22.5,
     "cpu_steal_careful": 50.0,
     "cpu_steal_critical": 90.0,
     "cpu_steal_warning": 70.0,
     "cpu_system_careful": 50.0,
     "cpu_system_critical": 90.0,
     "cpu_system_log": ["False"],
     "cpu_system_warning": 70.0,
     "cpu_total_careful": 65.0,
     "cpu_total_critical": 85.0,
     "cpu_total_log": ["True"],
     "cpu_total_warning": 75.0,
     "cpu_user_careful": 50.0,
     "cpu_user_critical": 90.0,
     "cpu_user_log": ["False"],
     "cpu_user_warning": 70.0,
     "history_size": 3600.0}

