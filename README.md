# CrispChat - A Python-Based Multi-Connection Chat Application

CrispChat is a real-time chat application that allows multiple users to connect and communicate with each other. Built using Python, it leverages sockets and the select module to handle multiple connections efficiently. The application consists of two main components: the client and the server.

## Features
- Multi-Connection Support: Allows multiple clients to connect and chat simultaneously.
- Real-Time Messaging: Enables real-time communication between connected users.
- User Authentication: Users can set their usernames for personalized chatting.
- Error Handling: Robust error handling to ensure smooth communication.
- Cross-Platform Compatibility: Works across different operating systems thanks to the use of the select module.

## Files
1. client.py
The client-side script that allows users to connect to the server, set their username, and send/receive messages.

2. server.py
The server-side script that listens for incoming connections, manages connected clients, and relays messages between them.

## Installation
1. Clone the Repository:
``` git clone https://github.com/username/CrispChat.git ```
2. Navigate to the Project Directory:
``` cd CrispChat ```
