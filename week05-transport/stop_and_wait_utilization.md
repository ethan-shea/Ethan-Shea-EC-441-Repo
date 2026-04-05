# Week 5 – Stop-and-Wait Link Utilization

Type: Problem  
Topic: Reliable Data Transfer (Stop-and-Wait)  
Layer: Transport Layer  

---

## Problem

A link has:
- Bandwidth B = 1 Gb/s  
- Round-trip time RTT = 600 ms  
- Packet size = 1500 bytes  

Compute the link utilization using the Stop-and-Wait protocol.

---

## Solution

First convert packet size to bits:

1500 bytes = 12,000 bits  

Transmission time:

ttx = packet size / bandwidth  
ttx = 12,000 / (1 × 10⁹) = 12 µs  

Now compute utilization:

U = ttx / (RTT + ttx)

Convert RTT:

RTT = 600 ms = 600 × 10⁻³ s  

So:

U = (12 × 10⁻⁶) / (600 × 10⁻³ + 12 × 10⁻⁶)

U ≈ 0.00002 = 0.002%

---

## Interpretation

The sender spends almost all of its time waiting for acknowledgments.

Even though the link supports 1 Gb/s, the effective throughput is extremely low.

---

## Key Insight

Stop-and-Wait performs very poorly when RTT is large compared to transmission time.

This is why pipelining like Go-Back-N and Selective Repeat is necessary to fully utilize high-speed networks.
