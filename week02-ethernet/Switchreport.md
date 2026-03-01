# Week 2 – Ethernet Switch Self-Learning

## The Problem

A switch must decide which port to forward a frame out of.
It does not know host locations in advance.

Instead of just doing manual configuration, Ethernet switches build
their forwarding table automatically.

---

## Learning Rule

When a frame arrives on port P with source MAC address X:

Record (X → P) in the forwarding table.

This is called self-learning.

---

## Forwarding Rule

When a frame arrives:

1. Look up the destination MAC in the table.
2. If found → forward to that port only.
3. If not found → flood all ports except the one it arrived on.
4. Broadcast or multicast → always flood.

Entries expire after a timeout (~300 seconds).

---

## Example

Three hosts A, B, C connected to a switch.
Table starts empty.

1. A sends to B  
   Switch learns A → port 1  
   B unknown → flood

2. B replies to A  
   Switch learns B → port 2  
   A known → forward only to port 1

3. C sends to A  
   Switch learns C → port 3  
   A known → forward only to port 1

After a few exchanges, the switch has learned all locations
and flooding stops.

---

## Key Insight

Switches are plug-and-play because of self-learning.
They require no configuration and adapt automatically
if hosts move to different ports.

This is why modern Ethernet networks scale efficiently
without manual MAC address configuration.
