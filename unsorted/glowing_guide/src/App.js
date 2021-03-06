import { useState } from "react";
import { BrowserRouter as Router, Link, Route, Switch } from "react-router-dom";
import "./App.css";
import About from "./components/About";
import Blog from "./components/Blog";
import Dashboard from "./components/Dashboard";
import Home from "./components/Home";
import Post from "./components/Post";
import { Login, UserDetail } from "./components/UserDetail";
import Weather from "./components/Weather";
import { BlogContext } from "./context/BlogContext";
export default function App() {
  let currentUser = {};
  const [user, setUser] = useState(currentUser);
  let posts = [
    {
      id: 1,
      owner: 164,
      is_public: false,
      publication_type: "CONCMNT",
      title: "The First Kempachi",
      content:
        "I found... A way to heal myself, so that I could enjoy fighting forever.",
      date_posted: "2021-07-04T14:32:05.161Z",
      date_expired: null,
      author: 164,
    },
    {
      id: 2,
      publication_type: "CONCMNT",
      is_public: false,
      owner: 171,
      title: "The Real Kempachi",
      content: "Feeling cute might kill Retsu Unohana later. IDK",
      author: 171,
    },
    {
      id: 3,
      is_public: true,
      publication_type: "ANNCMNT",
      owner: 137,
      title: "The new Commander",
      content: "I'm the new commander",
      author: 137,
    },
  ];

  return (
    <div className="App">
      <div className="App-header">
        {user ? <UserDetail user={user} /> : <Login setUser={setUser} />}
        <Router>
          <div>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/about">About</Link>
              </li>
              <li>
                <Link to="/dashboard">Dashboard</Link>
              </li>
              <li>
                <Link to="/weather">Weather</Link>
              </li>
              <li>
                <Link to="/blog">Blog</Link>
              </li>
            </ul>
            <hr />
            <Switch>
              <Route exact path="/" component={Home} />
              <Route exact path="/about" component={About} />
              <Route exact path="/weather" component={Weather} />
              <Route exact path="/dashboard" component={Dashboard} />
              <BlogContext.Provider value={posts}>
                <Route exact path="/blog" component={Blog} />
                <Route path="/blog/:id" component={Post} />
              </BlogContext.Provider>
            </Switch>
          </div>
        </Router>
      </div>
    </div>
  );
}
