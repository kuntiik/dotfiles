import React from "react";
import BotResponse from "./BotResponse";

const IntroSection = () => {
  return (
    <div id="introsection">
      <h1>
        Talk to Ned Flanders
        <BotResponse response=" - The Ultimate conversational budy" />
      </h1>
      <h2>
        A cutting-edge AI-powered app that provides instant answers to any
        question you may have. With Talkbot, you'll never be left searching for
        answers again. Whether you need information for school or work, or just
        want to know the latest news, Talkbot has you covered.
      </h2>
    </div>
  );
};

export default IntroSection;
