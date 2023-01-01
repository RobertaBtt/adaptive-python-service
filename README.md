Use this template everytime you want to quick setup a Python service.

This template is able to read from a SQLite, for the moment, 
and to read a configuration file.

From the main.py endpoint it is possible to call the services.

The service are available into the file services.py

This projects follows the Repository Pattern.
It is an abstraction over persistent storage.
Hides the details of data access.

The simples repository has just two methods, add() and get()

In the dependency inversio the domain model is free from the Infrastructure concerns.

Repository pattern is a simple abstraction
around permanent storage. Repository gives you the illusion of a collection of in-memory objects.

The Service Layer orchestrate our workflow and defines the Use Cases of our systems.
The service layer will become the main way to our app.

This is the architecture Layered Architecture, of type monolith.
Components are organized into logical horizontal layers and every layer consists of 4 standards layers:

Presentation
Business
Persistence
Database


Layers of isolation: changes made in one layer in the architecture, generally don't impact
or affect components in other layers.
Each layer is indipendent from the others.
