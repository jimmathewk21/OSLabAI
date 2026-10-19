documents = {
    "Process Scheduling": [
        "Process scheduling selects a process from the ready queue for execution by the CPU.",
        "FCFS stands for First Come First Served and executes processes in their arrival order.",
        "SJF stands for Shortest Job First and selects the process with the shortest CPU burst time.",
        "Round Robin scheduling assigns each process a fixed time quantum.",
        "Round Robin is suitable for time-sharing systems because processes receive CPU time in turns.",
        "Priority scheduling selects a process based on its priority.",
        "Preemptive scheduling allows the operating system to interrupt a running process.",
        "Non-preemptive scheduling allows a process to continue until it finishes or blocks.",
        "Turnaround time is the completion time minus the arrival time.",
        "Waiting time is the total time a process spends waiting in the ready queue.",
        "Response time is the time between submitting a request and receiving the first response."
    ],
    "Deadlocks": [
        "A deadlock occurs when processes wait indefinitely for resources held by other processes.",
        "The four necessary conditions for deadlock are mutual exclusion, hold and wait, no preemption, and circular wait.",
        "Mutual exclusion means a resource can be used by only one process at a time.",
        "Hold and wait occurs when a process holds one resource while waiting for another.",
        "No preemption means resources cannot be forcibly taken away from a process.",
        "Circular wait occurs when processes form a circular chain of resource dependencies.",
        "Deadlock prevention breaks at least one of the four necessary conditions.",
        "Deadlock avoidance checks whether allocating resources keeps the system in a safe state.",
        "The Banker's algorithm is a deadlock avoidance algorithm.",
        "Deadlock detection identifies whether a deadlock has occurred.",
        "Recovery from deadlock may involve terminating processes or preempting resources."
    ],
    "Memory Management": [
        "Memory management controls the allocation and deallocation of main memory.",
        "Paging divides logical memory into fixed-size pages and physical memory into frames.",
        "A page table maps logical pages to physical memory frames.",
        "Virtual memory allows a program to execute without requiring the entire program to be in RAM.",
        "A page fault occurs when a process accesses a page that is not currently available in physical memory.",
        "Demand paging loads a page into memory when it is needed.",
        "Internal fragmentation is unused space inside an allocated memory block.",
        "External fragmentation occurs when free memory is divided into small non-contiguous blocks.",
        "Segmentation divides a program into logical units such as code, data, and stack.",
        "FIFO page replacement removes the page that entered memory first.",
        "LRU page replacement removes the page that has not been used for the longest time."
    ],
    "Process Synchronization": [
        "Process synchronization coordinates processes that share data or resources.",
        "A critical section is a part of a program that accesses shared data.",
        "A race condition occurs when the result depends on the timing or order of concurrent operations.",
        "A semaphore is a synchronization mechanism that uses a counter to control access to resources.",
        "A mutex is a locking mechanism that allows only one thread at a time to access a protected section.",
        "The wait operation may decrease a semaphore value and block a process when access is unavailable.",
        "The signal operation releases a resource or wakes a waiting process.",
        "Mutual exclusion ensures that only one process at a time enters a protected critical section.",
        "Busy waiting occurs when a process repeatedly checks a condition instead of sleeping.",
        "The producer-consumer problem is a classic synchronization problem involving a shared buffer."
    ],
    "File Systems": [
        "A file system organizes and manages files and directories on storage devices.",
        "A file stores information such as text, programs, images, or other data.",
        "Directories organize files and can contain other directories.",
        "File permissions control who can read, write, or execute a file.",
        "Contiguous allocation stores a file in consecutive disk blocks.",
        "Linked allocation stores file blocks using links between blocks.",
        "Indexed allocation uses an index block to store the addresses of file blocks.",
        "Sequential access processes file data in order.",
        "Direct access allows a program to access a particular file location.",
        "Free-space management tracks disk blocks that are available for allocation."
    ],
    "Operating System Basics": [
        "An operating system, also called OS, manages computer hardware and provides services to application programs.",
        "The kernel is the core part of an operating system.",
        "A system call allows a program to request a service from the operating system.",
        "Multitasking allows multiple tasks to make progress during the same period.",
        "A process is a program in execution.",
        "A thread is a unit of execution within a process.",
        "User mode restricts access to privileged hardware operations.",
        "Kernel mode allows the operating system to perform privileged operations.",
        "An interrupt signals the CPU that an event needs attention.",
        "A context switch saves the state of one process or thread and restores another."
    ],
    "CPU and Process Concepts": [
        "A process moves through states such as new, ready, running, waiting, and terminated.",
        "The process control block stores information about a process.",
        "The CPU executes instructions belonging to running processes.",
        "The dispatcher gives control of the CPU to the process selected by the scheduler.",
        "Throughput is the number of processes completed per unit of time.",
        "CPU utilization measures the proportion of time the CPU is busy.",
        "A zombie process has completed execution but still has an entry awaiting collection by its parent.",
        "An orphan process continues running after its parent process terminates.",
        "A process is an independent program in execution, while a thread is a unit of execution within a process.",
        "Threads in the same process share resources, while separate processes generally have separate address spaces."
    ]
}

topic_keywords = {
    "Process Scheduling": {
        "process", "scheduling", "schedule", "fcfs", "sjf", "round",
        "robin", "priority", "quantum", "waiting", "turnaround",
        "preemptive", "nonpreemptive", "response", "burst", "arrival"
    },
    "Deadlocks": {
        "deadlock", "mutual", "exclusion", "circular", "banker",
        "prevention", "avoidance", "detection", "recovery", "resource",
        "safe", "wait"
    },
    "Memory Management": {
        "memory", "paging", "page", "fault", "virtual", "frame",
        "fragmentation", "segmentation", "replacement", "fifo", "lru",
        "ram", "demand"
    },
    "Process Synchronization": {
        "synchronization", "synchronize", "mutex", "semaphore", "race",
        "critical", "section", "producer", "consumer", "wait", "signal",
        "concurrency", "shared", "lock"
    },
    "File Systems": {
        "file", "system", "directory", "permission", "allocation",
        "contiguous", "linked", "indexed", "disk", "storage", "access",
        "sequential"
    },
    "Operating System Basics": {
        "operating", "system", "os", "kernel", "call", "multitasking",
        "thread", "mode", "interrupt", "hardware", "software", "process",
        "computer"
    },
    "CPU and Process Concepts": {
        "process", "thread", "cpu", "state", "control", "block",
        "dispatcher", "throughput", "utilization", "zombie", "orphan",
        "context", "switch", "difference", "compare", "comparison"
    }
}
