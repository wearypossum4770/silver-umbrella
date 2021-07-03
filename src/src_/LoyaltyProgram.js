class LoyaltyProgram{
    constructor({order_total=0,loyalty_points=0}){
        this.orderTotal = order_total
        this.pointTotal = loyalty_points
    }
    redeemPoints(redeem=0){
        if (redeem%100==0 && this.pointTotal-redeem>0){
            this.pointTotal-=redeem
            this.orderDiscount = Math.floor(redeem/100*5)   
        }
        else {
            this.rejectionMessage = "cannot redeem points"
        }
    }
    awardPoints(){
    this.pointTotal+=Math.floor(this.orderTotal)
    }
friendReferral(friend){
    this.pointTotal+=friend*100
}
weeklyRockefeller(){
    this.pointTotal+=100
}
}

let jake = {
    order_total:20.45,loyalty_points:0
}

let obj = new LoyaltyProgram(jake)
obj.awardPoints()
obj.redeemPoints(200)
console.log(obj)
