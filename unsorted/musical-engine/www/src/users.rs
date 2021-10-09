struct User {
    username:String,
    email:String,
    active:bool,
    first_name:String, 
    middle_name:String,
    last_name:String, 
    pk:i32,
    password:String,
    is_admin:bool,
    is_staff:bool,
    is_superuser:bool,
}
impl User {
    let options = ['create_superuser','create_user']
    pub fn create(){}
    pub fn update(){}
    pub fn find_all(){}
    pub fn destroy(){}
    pub fn find_by_id(){}
    pub fn create_user(){
        User {
            username:username,
            email:email,
            active:true,
            first_name:first_name, 
            middle_name:middle_name,
            last_name:last_name, 
            pk:pk,
            is_admin:false,
            is_staff:false,
            is_superuser:false,
        }
    }
}

let user1 = User {
pk: 83,
active:true,
username: "yara.greyjoy",
first_name: "yara",
email: "yara.greyjoy@game.of.thrones.com",
last_name: "greyjoy",
middle_name: '',
}