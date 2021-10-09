import { webcrypto } from "crypto";
const { subtle } = webcrypto;
export default async function generatekeypair() {
  const keyPair = await subtle.generateKey(
    {
      name: "ECDH",
      namedCurve: "P-256",
    },
    true,
    ["deriveKey", "deriveBits"],
  );
  const publicKeyJwk = await subtle.exportKey("jwk", keyPair.publicKey);

  const privateKeyJwk = await subtle.exportKey("jwk", keyPair.privateKey);
  console.log(publicKeyJwk);
  return { publicKeyJwk, privateKeyJwk };
}
