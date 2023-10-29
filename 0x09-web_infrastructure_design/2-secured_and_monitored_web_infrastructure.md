Components:
===========

Load Balancer (LB):
===================
Terminates SSL
Distributes traffic among web servers


Web Servers:
============

Nginx for serving web content
SSL certificate for HTTPS
Firewall (FW1, FW2, FW3) for security
Application Servers (AS1, AS2, AS3)


Database Servers (DB1, DB2, DB3)

MySQL databases

Monitoring Clients (MC1, MC2, MC3)

Data collectors for monitoring services



Explanation of the Infrastructure:

Why Add Three Firewalls: Firewalls are added to each component (web servers, application servers, and database servers) to restrict unauthorized access and enhance security. They act as a barrier between the servers and external threats.

Traffic Served Over HTTPS: HTTPS is used to encrypt data in transit, ensuring secure communication between the user's browser and the web servers. This protects sensitive information and builds trust with users.

Monitoring: Monitoring tools (Sumo Logic or others) are used to track the performance, health, and security of the infrastructure in real-time. They help identify issues, troubleshoot, and ensure optimal operation.

How Monitoring Tools Collect Data: Monitoring clients (MC1, MC2, MC3) collect data by continuously sending performance and log data to the monitoring service (Sumo Logic or others). The monitoring service processes and analyzes this data, providing insights and alerts.

Monitoring Web Server QPS (Queries Per Second): To monitor web server QPS, you can set up monitoring for the Nginx web server. Track incoming HTTP requests and measure the request rate over time. Create alerts for unusual spikes or drops in QPS.

Issues with this Infrastructure:

Terminating SSL at the Load Balancer Level: While terminating SSL at the load balancer can improve efficiency, it means that traffic between the load balancer and web servers is not encrypted. This poses a security risk, especially if the internal network is not fully trusted. Consider re-encrypting traffic between the load balancer and web servers for enhanced security.

Having Only One MySQL Server Capable of Accepting Writes: If only one MySQL server (e.g., DB1) can accept write operations, it creates a single point of failure for write-heavy applications. If DB1 fails, write operations will be disrupted. Implement a database replication and failover strategy to address this issue.

Servers with All the Same Components: Having servers with identical components (database, web server, and application server) may lead to inefficient resource allocation. Some servers may have underutilized components, while others may be resource-constrained. Consider customizing server roles based on their specific functions and resource needs to optimize performance and resource utilization.


