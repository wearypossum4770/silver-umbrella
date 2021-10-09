import { webcrypto } from "crypto";
import atob from "atob";
const { subtle } = webcrypto;

export default async function decryptMessage(messageJSON, derivedKey) {
  try {
    const message = JSON.parse(messageJSON);
    const text = message.base64Data;
    const initializationVector = new Uint8Array(message.initializationVector)
      .buffer;
    const string = atob(text);
    const uintArray = new Uint8Array(
      [...string].map(char => char.charCodeAt(0)),
    );
    const algorithm = {
      name: "AES-GCM",
      iv: initializationVector,
    };
    const decryptedData = await window.crypto.subtle.decrypt(
      algorithm,
      derivedKey,
      uintArray,
    );

    return new TextDecoder().decode(decryptedData);
  } catch (e) {
    return `error decrypting message: ${e}`;
  }
}
