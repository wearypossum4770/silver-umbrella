<template>
  <div></div>
</template>

<script>
export default {
  data() {
    return {
      customerID: "130",
      BillAddr: {
        Line4: "Middlefield, CA  94303",
        Line3: "5647 Cypress Hill Ave.",
        Line2: "Sonnenschein Family Store",
        Line1: "Russ Sonnenschein",
        Long: "-122.1141681",
        Lat: "37.4238562",
        Id: "95",
      },
      ShipAddr: {
        City: "Middlefield",
        Line1: "5647 Cypress Hill Ave.",
        PostalCode: "94303",
        Lat: "37.4238562",
        Long: "-122.1141681",
        CountrySubDivisionCode: "CA",
        Id: "25",
      },
      CustomerMemo: "Thank you for your business and have a great day!",
      DocNumber: "1037",
      PrintStatus: "NeedToPrint",
      taxDetails: {
        netAmountTaxable: 200,
        taxRate: 10,
      },
    };
  },
};
</script>

<style scoped></style>
