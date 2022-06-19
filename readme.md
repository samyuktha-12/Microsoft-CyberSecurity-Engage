## Microsoft Cyber Security engage
[``botnet.py``](botnet.py) is a sample botnet that sends DDoS attack on a chosen victim using Multithreading concept  

[``rootkit.c``](rootkit.c) is a very basic rootkit developed to intrepret and manipulate the system calls

[``main.cpp``](main.cpp) is a botnet analyzer

# Botnet Analyzer

**Identification of attacks**
In order to identify the attacks, it is necessary to store the connections in a data structure. It is useful to determine an Object Oriented representation of the problem. First of all, there are Nodes, which in this case are computers with a specific IP. There are also connections between the computers, and each connection has a Date and a number of occurrences.

The Graph data structure naturally allows to represent connections between different nodes in a network. It stores the information of each node in a vector, and in order to store the connections, an adjacency table is created. In this table, the rows represent sources while the columns are targets. Whenever there is a connection between to nodes, the slot obtained by the indexes of the source and the target are marked. This allows to represent directed connections.

One limitation that the graph has is that, typically, the number of nodes in the network must be known beforehand. In order to overcome this, the adjacency table was programmed to resize each time its capacity was reached in the doubleSize method, following the same principle as in resizing arrays (vectors).

However, this is not enough to solve the problem. Normally, an adjacency table only contains integers that indicate the weight of an Edge. In this case the timestamp forms an important part of the connection (almost its identifier). As there could be connections to the same target at several different times (all of them coming from the same source), there could be several Edges even between the same two nodes. Therefore, an Edge object was created, which stored a DateTime object pointer (the date and time of the connection), and the number of occurrences. The number of occurrences can be understood as the amount of requests from the source to the target in that particular instant. When this number was high in and Edge, there could have been an attack.

The adjacencies table was transformed so that each slot became a vector of Edge object pointers. This means that for a particular pair of source and target, there could be several connections at different times. The table could be understood as a three dimensional structure. The rows (length) corresponding to the sources, the columns (width) corresponding to the targets. Each slot is in reality a pointer to a vector, so it represents the depth. It is important to state that the number of edges is not fixed, so the slots have a variable depth each one, depending on the number of connections with distinct timestamp. This explains why in the ResizingVectorGraph , the adjacencies attribute was define as a triple pointer.

By using this modified structure, it is possible to identify attackers and print them to an output file ("attacks.txt"). This report shows all the potential attacks that happened in the network, stating the attacker IP, the date time, the number of attacks (i.e. the number of unsuccessful accesses or the weight of that particular edge), and the target IP.
