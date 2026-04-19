# Week 6 – Wireshark UDP DNS Analysis

Type: Lab  
Topic: Tools – Wireshark / DNS / UDP  
Layer: Transport / Application  

---

## Objective

Use Wireshark to capture and analyze DNS traffic and understand how DNS operates over UDP.

---

## Method

I used Wireshark to capture live network traffic on my Ethernet interface.

After starting the capture, I applied the filter:

udp.port == 53

This isolates DNS traffic, since DNS typically uses UDP port 53.

---

## Results

The capture showed multiple DNS queries and responses between my computer and a DNS server.

From the packets:

- Protocol: DNS (over UDP)  
- Source IP: my computer (168.122.128.205)  
- Destination IP: DNS server (128.197.253.126)  
- Destination Port: 53  
- Source Port: ephemeral (randomly assigned by the OS)  

Both queries and responses were visible.

The traffic included lookups to domains such as:
- Microsoft-related services  
- Google services  
- Other background application domains  

---

## Analysis

Each DNS query is sent from the client to the DNS server using UDP.

The server responds with information such as:
- IP addresses (A records)  
- Canonical names (CNAME records)  

For example, some responses included multiple CNAME mappings before resolving to a final IP address.

The presence of many DNS requests shows that multiple applications are continuously performing domain lookups in the background.

---

## Observations

- DNS operates without a connection setup (unlike TCP)  
- Queries and responses occur quickly and in pairs  
- Multiple DNS requests can occur simultaneously  
- Background applications generate DNS traffic even without direct user input  

---

## Key Insight

This lab demonstrates that DNS relies on UDP for fast, low-overhead communication and is actively used by many applications in the background to resolve domain names into IP addresses.
