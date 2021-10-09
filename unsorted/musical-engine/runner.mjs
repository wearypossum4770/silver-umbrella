import axios from "axios";

async function api() {
  try {
    const resp = await axios.get("http://localhost:3002/login");
    console.log(resp);
  } catch (error) {
    console.log(error);
  }
}

api();
