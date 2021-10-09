// combine states into centeralized store in vuex.
// http://bl.ocks.org/biovisualize/8187844
// https://www.codegrepper.com/code-examples/javascript/convert+base64+png+to+jpg+javascript
const moverStore = {
  state: () => ({
    firstName: "",
    middleName: "",
    lastName: "",
    suffix: "",
    email: "",
    phoneNumber: "",
    phoneType: "MOBILE",
    moverUUID: "",
  }),
  mutations: {},
  actions: {},
  getters: {},
};
const moverStore = {
  state: () => ({
    oldStreetAddress: "",
    oldCity: "",
    oldState: "",
    oldZipCode: "",
    oldUrbanizationName: "",
    oldPoBoxNumber: "",
    oldAddressUUID: "",
  }),
  mutations: {},
  actions: {},
  getters: {},
};

const coaMoveCombined = {
  state: () => ({
    dcoa: false,
    billingAddressType: "",
    businessName: "",
    businessAlias1: "",
    businessAlias2: "",
    businessAlias3: "",
    businessAlias4: "",
    informedDelivery: false,
    forwardType: "",
    moverType: "",
    startDate: "",
    stopDate: "",
  }),
  mutations: {},
  actions: {},
  getters: {},
};
export { moverStore };
export default coaMoveCombined;
