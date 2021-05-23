# Server-Client-python
This is a simple python based chat application. "server.py" should be executed 1st. Once you do that, it waits for the clients to get connected to it through "sockets".
Execute the "client1.py" next and enter your name as it asks for it. You can confirm that client1 has connected to server by checking the server as it reflects the connection established between it and clent1.
Follow the same approach with client2. "server.py" in execution shows that both clients can now wxchange texts between them through the server. serve here is the mediator through which clients can interchaange basic conversations.
To stop this, close any of the clients and the server. This interrupts the conversation exchange which confirms that that connection between clients, through server, is now ended.
