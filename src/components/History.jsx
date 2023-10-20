import React from "react"
import HistoryElement from "./HistoryElement";

const History = ({historyContent, historyOnClickFunction, sessionList}) => {

    const renderSessions = sessionList.map((session) => (
        <HistoryElement id={session.id} name={session.name} onClickFunction={historyOnClickFunction} key={session.id}/>
      ));

    return (
        <div className="history">
            <h3>History</h3>
            {/* <HistoryElement id={1} name="foo" onClickFunction={historyOnClickFunction}/> */}
            {renderSessions}
        </div>
    )
}

export default History;