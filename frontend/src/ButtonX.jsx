import { useState } from "react";

export default function ButtonX() {
    const [count, setCount] = useState(7)

    return (
        <>
            <button 
            type="button"
            className="counter"
            onClick={()=>setCount((count)=>count+1)}
            >
                count is {count}
            </button>
        </>
    )
}