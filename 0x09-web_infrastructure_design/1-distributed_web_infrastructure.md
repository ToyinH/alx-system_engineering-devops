Components:
===============

Server 1 (8.8.8.1):
======================
Web Server (Nginx)
Application Server
Application Files
Database (MySQL)


Server 2 (8.8.8.2):
====================

Web Server (Nginx)
Application Server
Application Files
Database (MySQL)

Distributes traffic to the two application servers (Server 1 and Server 2).


Explanation of the Infrastructure:
==================================

Why Add Two Servers: By adding two servers, we introduce redundancy and load distribution to improve reliability and handle more traffic.

Why Add a Load Balancer (HAproxy): The load balancer evenly distributes incoming web requests between the two servers. This ensures high availability and improved performance.

Distribution Algorithm: The load balancer is configured with a Round Robin distribution algorithm, which cycles through the available servers in sequence. This ensures an even distribution of requests.

Active-Active Setup vs. Active-Passive Setup:
==============================================

Active-Active Setup: Both application servers actively handle incoming requests simultaneously. In this setup, the load balancer routes traffic to both servers. This improves performance and redundancy.

Active-Passive Setup: One server actively handles requests while the other remains on standby. If the active server fails, the passive server takes over. This setup improves fault tolerance but may underutilize resources.

Database Primary-Replica Cluster:
The database is set up as a Primary-Replica (Master-Slave) cluster, where Server 2 is the Primary (Master) node, and Server 1 is the Replica (Slave) node.
The Primary node handles write operations, and the Replica node replicates data from the Primary node for read operations. This ensures data consistency and fault tolerance.
Difference Between Primary and Replica in Regards to the Application:

The application server on Server 1 communicates with the database's Replica node (Server 1) for read operations, reducing the load on the Primary database node (Server 2).
The application server on Server 2 communicates with the Primary database node (Server 2) for write operations.


Issues with this Infrastructure:
================================

Single Point of Failure (SPOF):
The load balancer could be a single point of failure. If it goes down, the application servers won't receive traffic. Implementing redundancy for the load balancer can mitigate this risk.

Security Issues:
No firewall mentioned: Implementing a firewall is essential to protect the servers from unauthorized access.
No HTTPS mentioned: Secure the website by adding SSL/TLS encryption with HTTPS to protect data in transit.

No Monitoring:
Lack of monitoring and alerting systems can make it challenging to detect and respond to issues promptly. Implement monitoring tools to proactively address potential problems and maintain system health.

