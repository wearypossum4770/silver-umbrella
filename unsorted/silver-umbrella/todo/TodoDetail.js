import { useParams } from "react-router-dom";
import todoinit from "../..//data/todoinit.json";
import { useState } from "react";
import "./todo_styles.css";
export default function TodoDetail() {
  let { todo_id } = useParams();
  let toggler = (toggle) => (toggle ? "" : "Un-");
  let init = todoinit.filter((_todo) => _todo.id === parseInt(todo_id)).pop();
  const [saving, setSaving] = useState(false);
  const [todo, setTodo] = useState(init);
  const postData = () => {
    let options = {
      headers: {
        // 'Content-Type': 'multipart/form-data',
        "Content-Type": "application/json",
      },
      mode: "cors",
      method: "POST",
      body: JSON.stringify(todo),
    };
    let url = `http://127.0.0.1:8000/todos/${todo.id}/edit`;

    async function fechData() {
      try {
        setSaving(true);
        const resp = await (await fetch(url, options)).json();
      } catch (err) {
        console.log(err);
      }
    }
    fechData();
  };
  const getFile = ({ target: { files } }) =>
    setTodo({ ...todo, attachment: files[0] });
  const handleChange = ({ target: { name, value } }) =>
    setTodo({ ...todo, [name]: value });

  return (
    <div className="w3-row-padding">
      <form onSubmit={(e) => e.preventDefault()} encType="multipart/form-data">
        <div className="w3-card-4 w3-dark-grey">
          <div className="w3-container w3-center">
            <div className="w3-third w3-margin-left">
              <label htmlFor="title">Title:</label>
              <input
                className="w3-input w3-grey"
                name="title"
                value={todo.title}
                onChange={handleChange}
              />
            </div>
            <div className="w3-third w3-margin-left">
              <label htmlFor="content">Content:</label>
              <input
                className="w3-input w3-grey"
                name="content"
                value={todo.content}
                onChange={handleChange}
              />
            </div>
            <div className="w3-third w3-margin-left">
              <label id="completed" htmlFor="mark completed">
                Completed?
              </label>
              <input
                className="w3-check"
                id="completed"
                name="completed"
                type="checkbox"
                onChange={() =>
                  setTodo({ ...todo, completed: !todo.completed })
                }
                checked={todo.completed}
              />
            </div>
            <div className="w3-col">
              <label htmlFor="attachment">
                Add Attachment
                <input id="attachment" onChange={getFile} type="file" />
                📎
              </label>
              <button onClick={postData} className="w3-btn w3-green">
                {`Sav${saving ? "ing" : "e"} 💾`}{" "}
              </button>
              <button
                onClick={() =>
                  setTodo({ ...todo, isArchived: !todo.isArchived })
                }
                className="w3-btn w3-indigo"
              >{`Mark as ${toggler(todo.isArchived)} Archived 📇`}</button>
              <button
                onClick={() => setTodo({ ...todo, isDeleted: !todo.isDeleted })}
                className="w3-btn w3-red"
              >{`Mark as ${toggler(todo.isDeleted)} Deleted 🗑️`}</button>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}
