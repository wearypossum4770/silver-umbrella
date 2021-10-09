class User {
    constructor({
password= "",
username= "",
first_name= "",
email= "",
date_joined= "",
last_name= "",
middle_name= "",
title= "",
suffix= "",
date_of_birth= "",
is_patient= "",
is_clinic_staff= "",
date_of_death= "",
    }){
        this.password = password 
        this.username = username 
        this.first_name = first_name 
        this.email = email 
        this.date_joined = date_joined 
        this.last_name = last_name 
        this.middle_name = middle_name 
        this.title = title 
        this.suffix = suffix 
        this.date_of_birth = date_of_birth 
        this.is_patient = is_patient 
        this.is_clinic_staff = is_clinic_staff 
        this.date_of_death = date_of_death 
    }
    clean(){

 if (this.date_joined.length>0){
     this.date_joined = new Date(this.date_joined)
 }
 if (this.date_of_birth.length>0){
     this.date_of_birth = new Date(this.date_of_birth)
 }
 if (this.date_of_death.length>0){
     this.date_of_death = new Date(this.date_of_death)
 }
    }
}

export const user = (init) => new User(init)