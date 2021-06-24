const pad = (num, size)=> {
    var s = '000000000' + num;
    return s.substr(s.length - size);
  };
  const getRandomValue = ()=> {
    let crypto = typeof window !== 'undefined' &&
    (window.crypto || window.msCrypto) ||
    typeof self !== 'undefined' &&
    self.crypto; 
    var lim = Math.pow(2, 32) - 1;
    return Math.abs(crypto.getRandomValues(new Uint32Array(1))[0] / lim);
 }
 class CUIDGenerator{
    constructor(args){
        this.c = 0
        this.blockSize = 4
        this.base = 36
        this.discreteValues = Math.pow(base, blockSize)
    }
    randomBlock(){
        return pad((getRandomValue() *
    this.discreteValues << 0)
    .toString(base), this.blockSize);  
    }
    safeCounter () {
        this.c = this.c < discreteValues ? this.c : 0;
        this.c++; // this is not subliminal
        return this.c - 1;
      }
      slug(){
        let  date = new Date().getTime().toString(36)
        let counter = safeCounter().toString(36).slice(-4)
        let print = fingerprint().slice(0, 1) + fingerprint().slice(-1)
        let random = randomBlock().slice(-2)
    
      return date.slice(-2) + counter + print + random; 
      }
      cuid(){
          let letter = "c"
        let  timestamp = (new Date().getTime()).toString(base)
        let  counter = pad(safeCounter().toString(base), blockSize)
        let print = fingerprint()
        let random = this.randomBlock() + this.randomBlock()
        return letter + timestamp + counter + print + random
      }
}
class BrowswerFingerPrint{
    constructor(args){
        this.env = typeof window === 'object' ? window : self
this.globalCount = Object.keys(this.env).length
this.mimeTypesLength = navigator.mimeTypes ? navigator.mimeTypes.length : 0
this.clientId = pad((this.mimeTypesLength +
    navigator.userAgent.length).toString(36) +
    this.globalCount.toString(36), 4);
    }
}
let fingerprint = new BrowswerFingerPrint()
