import { useForm, SubmitHandler } from "react-hook-form";
const fields = [{field:"first_name", required:false, validate:false,},
{field:"middle_name", required:false, get validation(){},validate:false,},
{field:"last_name", required:false, get validation(){},validate:false,},
{field:"madien_name", required:false, get validation(){},validate:false,},
{field:"nickname", required:false, get validation(){},validate:false,},
{field:"suffix", required:false, get validation(){},validate:false,},
{field:"password", required:false, get validation(){},validate:false,},
{field:"username", required:false, get validation(){},validate:false,},
{field:"email", required:false, get validation(){},validate:false,},
{field:'title', required:false, get validation(){},validate:false,},
{field:'honorific_prefix', required:false, get validation(){},validate:false,},
{field:'honorific_suffix', required:false, get validation(){},validate:false,},
{field:'date_of_birth', required:false, get validation(){},validate:false,},
{field:'do_not_contact', re,quired:false, get validation(){},validate:false,}]
let schema = yup.object().shape({
    middle_name: yup.string(),
    last_name: yup.string(),
    madien_name: yup.string(),
    nickname: yup.string(),
    suffix: yup.string(),
    password: yup.string(),
    username: yup.string(),
    email: yup.string(),
    title: yup.string(),
    honorific_prefix: yup.string(),
    honorific_suffix: yup.string(),
    date_of_birth: yup.string(),
    do_not_contact: yup.string(),
})
export default function Singup(){
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
const onSubmit = data =>console.log(data)
return (
    <form onSubmit={handleSubmit(onSubmit)}>

    <label htmlFor="first_name">
        <input name="first_name"/>
    </label>
    <label htmlFor="middle_name">
        <input name="middle_name"/>
    </label>
    <label htmlFor="last_name">
        <input name="last_name"/>
    </label>
    <label htmlFor="madien_name">
        <input name="madien_name"/>
    </label>
    <label htmlFor="nickname">
        <input name="nickname"/>
    </label>
    <label htmlFor="suffix">
        <input name="suffix"/>
    </label>
    <label htmlFor="password">
        <input name="password"/>
    </label>
    <label htmlFor="username">
        <input name="username"/>
    </label>
    <label htmlFor="email">
        <input name="email"/>
    </label>
    <label htmlFor='title'>
        <input name='title'/>
    </label>  
    <label htmlFor='honorific_prefix'>
        <input name='honorific_prefix'/>
    </label>  
    <label htmlFor='honorific_suffix'>
        <input name='honorific_suffix'/>
    </label>  
    <label htmlFor='date_of_birth'>
        <input name='date_of_birth'/>
    </label>  
    <label htmlFor='do_not_contact'>
        <input name='do_not_contact'/>
    </label> 
    {errors.exampleRequired && <span>This field is required</span>}

<input type="submit" />
    </form>
) 
    }

    