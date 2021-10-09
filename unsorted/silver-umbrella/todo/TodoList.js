import { useState, useEffect, useContext } from "react";
import { useHistory } from "react-router-dom";
import { AuthenticationContext } from "../../context/AuthenticationContext";

export default function TodoList() {
  let history = useHistory();
  const { credentials,userMemo } = useContext(AuthenticationContext);
  
  const [isLoading, setIsLoading] = useState(true);
  const [display, setDisplay] = useState();
  const [todos, setTodos] = useState([]);
  const handleChange = (e) => null;
  useEffect(() => {
    let options = {
      headers: {
        // 'Content-Type': 'multipart/form-data',
        "Content-Type": "application/json",
        "Authorization": `Token ${userMemo.user.auth_token}`, 
      },
      mode: "cors",
    };
    let url = `http://127.0.0.1:8000/todos/`;
    async function fechData() {
      try {
        const resp = await (await fetch(url, options)).json();
        console.log(resp);
        if (resp.detail !== "Authentication credentials were not provided.") {
          setTodos(resp);
          setIsLoading(false);
        }
      } catch (err) {
        console.log(err);
      }
    }
    fechData();
  }, []);
  return (
    <div className="todo-container">
      <div className="select">
        <select
          onSelect={({ target: { value } }) => setDisplay(value)}
          onChange={({ target: { value } }) => setDisplay(value)}
          name="todos"
          className="filter-todo"
        >
          <option value="all">All</option>
          <option value="completed">Completed</option>
          <option value="uncompleted">Uncompleted</option>
          <option value="archived">Archived</option>
          <option value="deleted">Deleted</option>
        </select>
      </div>
      <ul type="none" className="todo-list">
        {isLoading
          ? null
          : [  {
            "isLocal": false,
            "id": 1,
            "isDeleted": true,
            "title": "Learn React",
            "content": "Learn React",
            "isArchived": true,
            "completed": true
          },].map((todo) => (
              <li
                key={todo.id}
                onClick={() => history.push(`/todos/${todo.id}`)}
                className="w3-bar"
              >
                <input
                  type="checkbox"
                  // onClick="this.parentElement.style.display='none'"
                  onChange={handleChange}
                  className="w3-bar-item w3-button w3-xlarge w3-right"
                  checked={todo.completed}
                />
                <span
                  className="w3-bar-item w3-circle"
                  style={{ width: "85px" }}
                >
                  {todo.id}
                </span>
                <div className="w3-bar-item">
                  <span className="w3-large">{todo.content}</span>
                  <br />
                  {/* <span>Web Designer</span> */}
                </div>
              </li>
            ))}
      </ul>
    </div>
  );
}
