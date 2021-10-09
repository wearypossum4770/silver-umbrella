import { webcrypto, getDiffieHellman } from "crypto";
const { subtle } = webcrypto;
const alice = getDiffieHellman("modp15");
const bob = getDiffieHellman("modp15");
alice.generateKeys();
bob.generateKeys();
const aliceSecret = alice.computeSecret(bob.getPublicKey(), null, "hex");
const bobSecret = bob.computeSecret(alice.getPublicKey(), null, "hex");
console.log(alice.getPrime().toString("hex").length * 4);
