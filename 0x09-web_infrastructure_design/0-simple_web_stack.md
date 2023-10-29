<0. Simple web stack>
=======================

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

Attached is an image of a whiteboard to design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Here is an explanation by having a user wanting to access your website.

Components:
===========

1. Server: The server is a physical or virtual machine responsible for hosting the entire web infrastructure. In this case, it is a single server.

Web Server (Nginx): Nginx is responsible for handling HTTP requests and serving static content. It listens for incoming requests and forwards them to the application server when dynamic content is required.

Application Server: This component is responsible for executing server-side code (e.g., PHP, Python, Ruby) to generate dynamic content based on user requests.

Application Files (Your Code Base): These are the code and files that make up your website. They include HTML templates, application logic, and other assets.

Database (MySQL): MySQL is used to store and retrieve data for the web application. It's essential for managing user data, content, and other information.

Domain Name (www.foobar.com): The domain name is the human-readable address users will use to access your website. It's configured with a "www" DNS record that points to your server's IP address (e.g., 8.8.8.8).

Explanation of the Infrastructure:
==================================

What is a Server? A server is a computer that stores and manages data, services, and resources, serving as the central point of the web infrastructure.

Role of the Domain Name: The domain name (www.foobar.com) is the human-friendly address that users type in their browsers to access the website. It's a user-friendly alias for the server's IP address.

Type of DNS Record www in www.foobar.com: The "www" in www.foobar.com is a subdomain, and it's typically a CNAME (Canonical Name) record that points to the IP address of the server where your website is hosted.

Role of the Web Server (Nginx): Nginx acts as a reverse proxy, receiving and forwarding HTTP requests to the application server. It's also responsible for serving static content like images and CSS.

Role of the Application Server: The application server runs server-side code, processes user requests, communicates with the database, and generates dynamic content to be sent back to the user's browser.

Role of the Database (MySQL): The database stores and manages data. It's used for storing and retrieving information such as user accounts, content, and any other data required by the application.

Communication with the User's Computer: The server communicates with the user's computer via HTTP. When a user requests a page from www.foobar.com, their browser sends an HTTP request to the server. The server processes the request, generates the appropriate response, and sends it back to the user's browser over the internet.

Issues with this Infrastructure:
================================

Single Point of Failure (SPOF): This architecture has a single server, which is a potential single point of failure. If the server goes down, the entire website becomes inaccessible. To address this, redundancy or failover mechanisms can be implemented.

Downtime During Maintenance: During maintenance, such as deploying new code, the web server may need to be restarted. This can result in temporary downtime, affecting user access. Load balancing or staging environments can help minimize such downtime.

Scalability Limitations: This infrastructure may struggle to handle a sudden influx of traffic. Scaling is challenging with only one server. To address this, you can implement load balancing and, if necessary, migrate to a more scalable architecture, such as a cloud-based solution with auto-scaling capabilities.