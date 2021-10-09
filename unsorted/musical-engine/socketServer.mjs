import { WebSocketServer } from "ws";
import { eventData, easterEggs } from "./www/sockets/helpers.mjs";
import {
  toJSON,
  heartbeat,
  noop,
  channels,
  parseJSON,
  getEasterEgg,
} from "./www/sockets/methods.mjs";
const PORT = 7625;
const wss = new WebSocketServer({ port: PORT });

// wss.on('upgrade', (req, socket, head)=>{

//   console.log('request follows\n\n\n')
//   console.log(req)
//   console.log('socke follows \n\n\n')
//   console.log(socket)
//   console.log('head follows\n\n\n')
//   console.log(head)
// })

wss.on("connection", (ws, req, client) => {
  console.log("request information\n\n\n");
  let routes = channels(req.url);

  console.log(routes);
  ws.on("message", msg => {
    console.log("messag information\n\n\n");
    console.log(msg);
    ws.isAlive = true;
    ws.on("pong", heartbeat);
    const { message } = parseJSON(msg);
    let egg = getEasterEgg(message, easterEggs);
    if (egg) {
      ws.send(toJSON({ message: egg }));
    }
    console.log(`Received message ${message} from user ${client}`);
  });
  ws.send(toJSON({ message: "connected" }));
});
const interval = setInterval(function ping() {
  wss.clients.forEach(function each(ws) {
    if (ws.isAlive === false) return ws.terminate();
    ws.isAlive = false;
    ws.ping(noop);
  });
}, 30000);
wss.on("close", () => {
  clearInterval(interval);
});
