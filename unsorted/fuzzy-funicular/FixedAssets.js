// capitalizedInterest additional cost of assests.
// qualifyingAsset
// https://www.double-entry-bookkeeping.com/fixed-assets/capitalized-interest/
let avoidableInterest = 10
let actualInterest = 5 
// principal = weighted average accumulated expenditure
let interestCost = ({principal,rate,time})=>principal*rate*time
let capitalizedInterest = Math.min(actualInterest,avoidableInterest)
console.log(capitalizedInterest)
let petty_cash = {
    department:"",
    month:'',
    description:'',
    quantity:'',
    amount:'',
    notes:'',
}
let pettyCashReconciliation = {
    totalPettyCash:0,
    paidVouchersCounted:0,
    totalPettyCashAndVouchers:0,
    difference:0,
    preparedBy:'',
    preparationDate:new Date(),
}