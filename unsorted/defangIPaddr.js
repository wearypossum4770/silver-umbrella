export default function defangIPaddr(address) {
  return address.replace(/\./g, "[.]");
}
