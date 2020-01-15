# IoT_Network
*Available Project expansion:  
Implement client software for boards not capable of having an OS (eg. Arduino)*  

# Development of a small IoT Network

### Gateway
NVidia Jetson Nano or another board with high computing power, preferably with a GPU.

### Nodes
Raspberry, Beagleboard and other boards capable of having a Linux OS.

# Use
The basic idea is that a Node (client), running client software, can take an input from the user and send it to the Gateway (server). Then this passes the input to an executable and as soon as the executable finishes the execution, the Gateway sends the output to the Node (client) and the user can see it.

# Expand the project
Clone repository or download  

Run
```console
$ make
```
to compile the project.

To start the **server** run

```python
python3 server.py
```

To start a **client** run
```python
python3 client.py
```

### test_exec
This is a simple program to check the communication between the node and the server. It should be in the server side.

You can change this executable with one of your own choice, which takes an argument.
