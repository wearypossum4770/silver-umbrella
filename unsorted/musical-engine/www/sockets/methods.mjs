const toJSON = (obj = {}) => JSON.stringify(obj);
const parseJSON = (stringInit = "") => JSON.parse(stringInit);
const getEasterEgg = (msg, eggs) =>
  eggs.get(msg.toString().toLowerCase().trim());
const channels = url =>
  url.match(
    /\/(?<protocol>ws)\/(?<is_chat>chat)\/(?<chat_type>public|private)\/(?<username>.*)\/(?<room_group_name>.*)\/(?<channel_name>.*)\/(?<room_name>.*)\//,
  );
function noop() {}
function heartbeat() {
  this.isAlive = true;
}
export { heartbeat, noop, channels, toJSON, parseJSON, getEasterEgg };
