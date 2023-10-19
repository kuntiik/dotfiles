import React from "react";



const HistoryElement = ({id, name}) => {
    function logIdAndName() {
        // Log the id and name to the console
        console.log("Button ID: " + id);
        console.log("Button Name: " + name);
    }

    return (
        <button id={id} name={name} onClick={() => {console.log(id)}} >{name}</button>
    )
}

export default HistoryElement;