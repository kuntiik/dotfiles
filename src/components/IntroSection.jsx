import React from "react";
import BotResponse from "./BotResponse";

const IntroSection = () => {
  return (
    <div id="introsection">
      <h1>
        Talk to Ned Flanders
        <BotResponse response=" - The Ultimate Conversational Budy" />
      </h1>
      <h2>
      Well, hi-diddly-ho there, neighborino! I'd like to take a moment to introduce you to our new chat bot, and let me tell you, it's chock-full of friendliness and positivity. Just like a cheerful morning in Springfield, this bot is here to brighten your day, answer your questions, and lend a hand with a warm digital smile that could make even Grampa Simpson grin.
      </h2>
    </div>
  );
};

export default IntroSection;
