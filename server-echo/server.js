// import library
const WebSocket = require("ws");

const PORT = 5000;

const wsServer = new WebSocket.Server({
  port: PORT,
});

// handles events from incoming client/s
wsServer.on("connection", function (socket) {
  //displays message when a client is connected
  console.log("A client just connected");

  //attach some behavior to the incoming socket
  socket.on("message", function (msg) {
    console.log("Received message from client: " + msg);

    //echos back to the client
    //socket.send("I am your echo!! " + msg);

    //broadcasts messages to all connected clients
    wsServer.clients.forEach(function (client) {
      client.send("Client says: " + msg);
    });
  });
});

console.log(new Date() + " Server is listening on port " + PORT);
