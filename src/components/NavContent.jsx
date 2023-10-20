import React from "react";
import NavLinksContainer from "./NavLinksContainer";
import NavPrompt from "./NavPrompt";
import NewChat from "./NewChat";
import Settings from "./Settings"
import History from "./History";

const NavContent = ({ chatLog, setChatLog, setShowMenu, historyOnClickFunction, sessionList }) => {
  return (
    <>
      <NewChat setChatLog={setChatLog} setShowMenu={setShowMenu} />
      <div className="navPromptWrapper">
        {chatLog.map(
          (chat, idx) =>
            chat.botMessage && (
              <NavPrompt chatPrompt={chat.chatPrompt} key={idx} />
            )
        )}
      </div>
      <NavLinksContainer chatLog={chatLog} setChatLog={setChatLog} />
      <History historyOnClickFunction={historyOnClickFunction} sessionList={sessionList}/>
      <Settings/>
    </>
  );
};

export default NavContent;
