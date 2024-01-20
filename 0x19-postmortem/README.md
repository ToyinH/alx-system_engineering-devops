# 0x19. Postmortem


# Postmortem For A Website Outage 

![incident report](image.png)

This is the postmortem to the website outage we experienced on Thursday, Jan 18, 2024, by 3:05 am WAT.

## Issue Summary:
The outage occurred on Thursday, Jan 18, 2024, by 3:05 am WAT and lasted for 30 minutes. The website experienced a complete service outage during this period. Users were unable to access the site, leading to a 100% decrease in user engagement. The root cause of the outage was a sudden and unexpected traffic spike that overwhelmed the website's infrastructure from users’ registration for a free offer on the site.

## Timeline (all time in WAT):
- 3:05 am: Outage began
- 3:05 am: The issue was detected through an automated monitoring tool, indicating a surge in traffic.
- 3:05 am:  Monitoring tools alerted the call team. 
- 3:05 am: The team investigated the issue, focusing on identifying the source of the traffic spike. Initial assumptions pointed towards a potential DDoS attack, leading to a thorough analysis of incoming requests.
- 3:15 am: The incident was escalated.
- 3:25 am: Traffic spike due to user registration for a free product detected. Server added and other servers restarted with a Load Balancer configured.
- 3:35 am: Website back online. 
- 3:35 am: Monitor configured to monitor web traffic, load balancers and servers’ memory. 

## Root Cause and Resolution:
The primary cause of the outage was an unexpected surge in legitimate user traffic resulting from a sudden increase in the popularity of the site on social media. As the site’s product is trending. The immediate solution involved scaling up server resources to handle the additional load and optimising the load balancer algorithm to distribute traffic more efficiently.

## Corrective and Preventive Measures:
- Getting additional servers
- Improving the load balancer algorithms 
- Setup to dynamically scale load balancer if one is down
- Enhance traffic monitoring and servers’ memory usage monitoring
- Prompt alert when web resources are being used up before the site is down. 

In conclusion, the website outage resulted from a sudden traffic spike. This has been resolved, and provisions have been made to prevent future reoccurrences. 