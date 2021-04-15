"""
In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a
load balancer that ensures that there are enough servers to serve those connections.

To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is
represented by an id, that could, for example, be the IP address of the computer connecting to the server.
For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

Run the following code that defines this Server class.

"""

#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id]=connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for item in self.connections.values():
            total=total+item

        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


#Now run the following cell to create a Server instance and add a connection to it, then check the load:

server = Server()
server.add_connection("192.168.1.1")

print(server.load())


"""
Alright, we now have a basic implementation of the server class. Let's look at the basic LoadBalancing class.
This class will start with only one server available. When a connection gets added, it will randomly select a server to
serve that connection, and then pass on the connection to the server. The LoadBalancing class also needs to keep track
of the ongoing connections to be able to close them. This is the basic structure:
"""

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()


    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load=0
        total_ser=0

        for server in self.servers:
            total_load=float(total_load)+server.load()
            total_ser+=1

        return total_load/total_ser

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load()>50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())