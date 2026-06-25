import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState([])

  useEffect(()=>{
    fetch('http://localhost:8000/movies')
    .then(resp => resp.json())
    .then(json => setData(json))
    .catch(error => console.error('Error fetching data:', error))
  }, [])

  return (
    <ul>
      {data.map(item => (
        <li key={item.show_id}>{item.title}</li>
      ))}
    </ul>
  );
}

export default App
