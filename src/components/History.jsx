import React from "react"
import HistoryElement from "./HistoryElement";

const History = ({historyContent, historyOnClickFunction, sessionList}) => {

    const renderSessions = sessionList.map((session) => (
        <HistoryElement id={session.id} name={session.name}/>
      ));

    return (
        <div>
            <h3>History</h3>
            {/* <HistoryElement id={1} name="foo" onClickFunction={historyOnClickFunction}/> */}
            {renderSessions}
        </div>
    )
}

export default History;