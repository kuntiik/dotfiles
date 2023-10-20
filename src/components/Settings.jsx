import React, { useState } from 'react';
import './CollapsibleTextBox.css'; // Import your CSS file

function Settings({fields, setFields}) {
  const handleFieldChange = (fieldName, value) => {
    setFields({ ...fields, [fieldName]: value });
  };

  return (
    <div className="settingsContainer">
      <h3>Settings</h3>

      <div className="numberBox">
        <h3>Temperature:</h3>
        <input
          type="text"
          value={fields.temperature}
          onChange={(e) => handleFieldChange('temperature', e.target.value)}
          placeholder="non-collapsible text"
        />
      </div>

      <div className="numberBox">
        <h3>Max tokens</h3>
        <input
          value={fields.maxTokens}
          onChange={(e) => handleFieldChange('maxTokens', e.target.value)}
          placeholder="non-collapsible text"
        />
      </div>

      <div className='checkBox'>
        <h3>Input safety: </h3>
        <input
          type="checkbox"
          checked={fields.inputSafety}
          onChange={() => handleFieldChange('inputSafety', !fields.inputSafety)}
        />
      </div>
      <div className='checkBox'>
        <h3>Output safety: </h3>
        <input
          type="checkbox"
          checked={fields.outputSafety}
          onChange={() => handleFieldChange('outputSafety', !fields.outputSafety)}
        />
      </div>
    </div>
  );
}

export default Settings;