//consider using datagrid from mui

import { useState, useEffect } from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper
} from '@mui/material'

import './App.css'

function App() {
  const [data, setData] = useState([])

  useEffect(()=>{
    fetch('http://localhost:8000/movies')
    .then(resp => resp.json())
    .then(json => setData(json))
    .catch(error => console.error('Error fetching data:', error))
  }, [])

   const columns = data.length > 0 ? Object.keys(data[0]) : []

  return (
    <TableContainer component={Paper}>
      <Table>

        <TableHead>
          <TableRow>
            {columns.map(column => (
              <TableCell key={column}>
                {column}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>

        <TableBody>
          {data.map(row => (
            <TableRow key={row.show_id}>
              {columns.map(column => (
                <TableCell key={column}>
                  {row[column]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>

      </Table>
    </TableContainer>
  )
}

export default App
