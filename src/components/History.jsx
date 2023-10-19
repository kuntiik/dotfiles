import React from "react"
import HistoryElement from "./HistoryElement";

const History = ({historyContent, historyOnClickFunction}) => {
    return (
        <div>
            <h3>History</h3>
            <HistoryElement id={1} name="foo" onClickFunction={historyOnClickFunction}/>
        </div>
    )
}

export default History;