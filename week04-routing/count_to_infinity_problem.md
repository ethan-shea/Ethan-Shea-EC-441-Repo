# Week 4 – Count-to-Infinity in Distance Vector Routing

Type: Problem  
Topic: Routing – Distance Vector  
Layer: Network Layer  

---

## Problem

Consider a simple network:

A —1— B —1— C

Initially:
- dA(C) = 2 via B  
- dB(C) = 1 (direct)

Now suppose the link between B and C fails.

Show how the distance-vector algorithm leads to the count-to-infinity problem.

---

## Solution

After the link failure:

### Step 1
B detects the failure to C.

B checks neighbor A:
- A still believes dA(C) = 2

So B updates:
dB(C) = 1 + 2 = 3 (via A)

---

### Step 2
B tells A:
dB(C) = 3

A updates:
dA(C) = 1 + 3 = 4

---

### Step 3
A tells B:
dA(C) = 4

B updates:
dB(C) = 1 + 4 = 5

---

### Step 4
This continues:

- A → 6  
- B → 7  
- A → 8  
- ...

The cost increases indefinitely.

---

## Explanation

This happens because A and B rely on each other’s outdated information.
Each one believes the other has a valid path to C.

This creates a loop where packets bounce between A and B.

---

## Key Insight

Distance-vector routing has no built-in way to detect circular dependencies.

This leads to the “bad news travels slow” problem:
when a link fails, incorrect information can persist and slowly increase,
rather than converging.

Techniques like split horizon and poisoned reverse help reduce this issue,
but do not completely eliminate it.
