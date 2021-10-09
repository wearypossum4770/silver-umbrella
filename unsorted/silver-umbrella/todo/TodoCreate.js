import { useState } from "react";
import { useHistory } from "react-router-dom";

export default function TodoCreate() {
  let history = useHistory();
  const [todo, setTodo] = useState({
    title: null,
    content: null,
  });
  const [saving, setSaving] = useState(false);
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
    let url = `http://127.0.0.1:8000/todos/new/`;

    async function fechData() {
      try {
        if (todo?.title || todo?.content) {
          setSaving(true);
          const resp = await (await fetch(url, options)).json();
          if (resp) {
            history.push("/todos");
            return;
          }
        }
        setSaving(false);
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
                onChange={handleChange}
              />
            </div>
            <div className="w3-third w3-margin-left">
              <label htmlFor="content">Content:</label>
              <input
                className="w3-input w3-grey"
                name="content"
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
                checked={todo?.completed}
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
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}
