# Week 3 – Longest Prefix Match (LPM) Problem

Type: Problem  
Topic: Network Layer – Forwarding  
Layer: Network Layer  

---

## Problem

Given the following forwarding table:

| Prefix         | Next Hop |
|----------------|----------|
| 0.0.0.0/0      | A        |
| 10.0.0.0/8     | B        |
| 10.1.0.0/16    | C        |
| 10.1.2.0/24    | D        |

Determine the outgoing interface for each destination IP using longest prefix match:

1. 10.1.2.5  
2. 10.5.6.7  
3. 172.16.0.1  

---

## Solution

### 1. 10.1.2.5

Matches:
- 0.0.0.0/0  
- 10.0.0.0/8  
- 10.1.0.0/16  
- 10.1.2.0/24  

Longest prefix = /24 → Next Hop D  

---

### 2. 10.5.6.7

Matches:
- 0.0.0.0/0  
- 10.0.0.0/8  

Longest prefix = /8 → Next Hop B  

---

### 3. 172.16.0.1

Matches:
- 0.0.0.0/0  

Only match → Next Hop A  

---

## Main finding

Routers can find multiple matching entries, but always choose the most specific
and the longest prefix to match.

This allows routing tables to store both general routes like /8 and specific
routes like /24, which allows for efficient forwarding decisions.
