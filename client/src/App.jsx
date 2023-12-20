import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [userData, setUserData] = useState([]);

  useEffect(() => {
    apiData();
    }, []);

  const apiData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/user/api/");
      setUserData(res.data); // Assuming the response structure is { data: [...] }
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <>
    <ul>
      {userData.map((data) => (
        <li key={data.id}>
          {data.firstName} {data.lastName}
        </li>
        ))}
    </ul>
    </>
    );
}

export default App;
