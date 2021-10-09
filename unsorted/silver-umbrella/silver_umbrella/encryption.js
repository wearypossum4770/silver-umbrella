import {webcrypto as crypto} from 'crypto'
const publicExponent = new Uint8Array([1, 0, 1]);
const iv = await crypto.getRandomValues(new Uint8Array(16));
async function generateEcKey(namedCurve = 'P-521') {
    const {
      publicKey,
      privateKey
    } = await crypto.subtle.generateKey({
      name: 'ECDSA',
      namedCurve,
    }, true, ['sign', 'verify']);
  
    return { publicKey, privateKey };
  }
async function generateHmacKey(hash = 'SHA-256'){
    const key = await crypto.subtle.generateKey({
        name: 'HMAC',
        hash
      }, true, ['sign', 'verify']);
      return key;
    }

    async function generateRsaKey(modulusLength = 2048, hash = 'SHA-256') {
        const {
          publicKey,
          privateKey
        } = await crypto.subtle.generateKey({
          name: 'RSASSA-PKCS1-v1_5',
          modulusLength,
          publicExponent,
          hash,
        }, true, ['sign', 'verify']);
        return { publicKey, privateKey };
      }
      async function generateEd25519Key() {
        return crypto.subtle.generateKey({
          name: 'NODE-ED25519',
          namedCurve: 'NODE-ED25519',
        }, true, ['sign', 'verify']);
      }
      
      async function generateX25519Key() {
        return crypto.subtle.generateKey({
          name: 'ECDH',
          namedCurve: 'NODE-X25519',
        }, true, ['deriveKey']);
      }
      async function generateAesKey(length = 256) {
        const key = await crypto.subtle.generateKey({
          name: 'AES-CBC',
          length
        }, true, ['encrypt', 'decrypt']);
      
        return key;
      }
      async function encrypt(){
     let _types = [   'HmacKey',
     'RsaKey',
     'Ed25519Key',
     'X25519Key',]
      }