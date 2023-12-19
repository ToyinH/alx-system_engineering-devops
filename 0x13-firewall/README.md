# 0x13. Firewall

These tasks is on firewall for my webservers and load balancer

## 0. Block all incoming traffic but

Install ufw firewall and configure so that it blocks all incoming traffic,
except the following TCP ports:
- 22 (SSH)
- 443 (HTTPS SSL)
- 80 (HTTP)


## 1. Port forwarding
Configure server (web-01) so that its firewall redirects port 8080/TCP to port 80/TCP.
