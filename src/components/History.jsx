import React from "react"
import HistoryElement from "./HistoryElement";

const History = ({historyContent}) => {
    return (
        <div>
            <h3>History</h3>
            <HistoryElement id={1} name="foo"/>
        </div>
    )
}

export default History;