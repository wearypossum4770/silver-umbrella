const { writeFileSync, readFileSync } = require("fs")
const uuid = require("uuid")
class Task {
    constructor({_id,title="",content="",date_created=new Date(), date_due=null,date_modified=null, completed=false}){
this.external_id = uuid.v4()
this.pk = _id
this.model="tasks.task"
this.fields = {
    title,title,
content,content,
date_modified ,date_modified,
date_created,date_created,
date_due,date_due,
completed ,completed,
}





    }
}

let tasks = [
    {
        
        title:"personal list",
        content:"You",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Make a Todo List",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Cross off Item #2",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Steal steno pad from job",
        completed:false
    },
    {
        
        title:"personal list",
        contene:"",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Brainstorm to create a #5 task",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Surf the Internet",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Tell husband I sent out 10 resumes",
        completed:false
    },
    {
        
        title:"personal list",
        content:"Post 'unemployed stuff to do list' on the internet",
        completed:false
    },

    {title:"ITM304",content: "Quiz 6 SQL, Database Redesign", completed: true},
    {title:"ITM304",content: "Week 9 Problem Set # 4: Convert VARCHAR() string date to data type DATE", completed: true},
    {title:"ITM304",content: "Week 9 Problem Set # 4: Convert VARCHAR() string date to data type DATE", completed: true},
 
]
let file = "./users/fixtures/datainit.json"
let d = JSON.parse(readFileSync(file))
let data = tasks.map((task,id)=>new Task({_id:id+1,...task}))
let output = [...d,...data]
writeFileSync(file, JSON.stringify(output))