# Sets and Set Operations
# Overview:
# A set in Python is an unordered collection of unique elements.
#  It is useful for mathematical operations like union, intersection, and difference.
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
my_set.remove(3)  # Removing an element
# Practice Exercises and Examples
# Example: Managing a Dictionary of Server Configurations and Optimizing Retrieval
# Scenario:
# Suppose you are managing server configurations using a dictionary.
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
server_name = 'server1'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")