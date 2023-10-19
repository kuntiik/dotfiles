import React from "react";



const HistoryElement = ({id, name, onClickFunction}) => {
    function logIdAndName() {
        // Log the id and name to the console
        console.log("Button ID: " + id);
        console.log("Button Name: " + name);
        onClickFunction(id);
    }

    return (
        <button id={id} name={name} onClick={logIdAndName} >{name}</button>
    )
}

export default HistoryElement;