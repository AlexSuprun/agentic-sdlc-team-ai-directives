# Stateless Services

All services should be designed to be stateless, meaning they do not maintain any internal state between requests. This ensures scalability, reliability, and ease of deployment in cloud environments. State should be externalized to databases or caches as needed.