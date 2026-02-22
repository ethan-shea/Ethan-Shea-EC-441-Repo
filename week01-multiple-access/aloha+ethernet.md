# Week 1 – Pure ALOHA vs. Slotted ALOHA Efficiency and Ethernet Minimum Frame Size

## Objective
Derive and compare the maximum throughput of pure ALOHA and slotted ALOHA.

## Pure ALOHA

Throughput:
S = G e^{-2G}

Differentiate:
dS/dG = e^{-2G}(1 − 2G)

Set equal to 0:
1 − 2G = 0  ⇒  G = 1/2

Maximum throughput:
S_max = (1/2)e^{-1} = 1/(2e) ≈ 0.184

Maximum efficiency ≈ 18%

Collision window = 2T

---

## Slotted ALOHA

Throughput:
S = G e^{-G}

Differentiate:
dS/dG = e^{-G}(1 − G)

Set equal to 0:
1 − G = 0  ⇒  G = 1

Maximum throughput:
S_max = e^{-1} = 1/e ≈ 0.368

Maximum efficiency ≈ 37%

Collision window = T

---

## Key Insight

Slotted ALOHA halves the collision window from 2T to T,
which doubles the maximum efficiency:

1/e ÷ (1/(2e)) = 2

Therefore, slotted ALOHA is 2 times more efficient than pure ALOHA!

This is important because a simple synchronization rule doubles the amount of usable capacity without changing the underlying channel. 
It shows how one protocol design change can massively improve efficiency.

---

# Ethernet Minimum Frame Size

## Requirement for Collision Detection

For CSMA/CD to work, a node must still be transmitting when a collision signal
returns from the farthest node.

Therefore:

Transmission time ≥ round-trip propagation delay

T ≥ 2τ

Since T = L / R:

L / R ≥ 2τ

Multiply both sides by R:

L ≥ 2τR

---

## Classic Ethernet Parameters

R = 10 Mb/s  
Maximum segment length ≈ 2500 m  
Propagation speed ≈ 2 × 10^8 m/s  

One-way delay:
τ = 2500 / (2 × 10^8) ≈ 12.5 μs  

With system margin:
τ ≈ 25 μs  

Minimum frame size:

L ≥ 2 × 25 μs × 10 Mb/s  
L ≥ 500 bits ≈ 64 bytes  

---

## Key Insight

The 64-byte Ethernet minimum frame size is not arbitrary.
It comes directly from propagation physics:

A node must still be transmitting when the worst-case
collision signal returns.

This still remains in modern Ethernet
even though switched full-duplex Ethernet no longer
uses CSMA in the real world.
