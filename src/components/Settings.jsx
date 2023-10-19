import React, { useState } from 'react';
import './CollapsibleTextBox.css'; // Import your CSS file

function Settings() {
  const [fields, setFields] = useState({
    isCollapsed: true,
    nonCollapsibleText: 100,
    isChecked: true,
  });

  const [isCollapsed, setIsCollapsed] = useState(false);

  const toggleCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  const handleToggleCollapse = () => {
    setFields({ ...fields, isCollapsed: !fields.isCollapsed });
  };

  const handleFieldChange = (fieldName, value) => {
    setFields({ ...fields, [fieldName]: value });
  };

  return (
    <div className="settingsContainer">
      <h1>Settings</h1>
      <div className="prompt">
        <div className="promptBox">
        <label>Prompt</label>
        <button onClick={handleToggleCollapse}>
          {fields.isCollapsed ? 'expand' : 'collapse'}
        </button>
        </div>
        <br />
        {fields.isCollapsed ? null : (
          <input
            type="text"
            placeholder="### instruction:
            use the following input and come up with a structured response in the style of ned flanders given the context.
            ### context:
            {input}

            ### input:
            {context}
            
            ### response:
            "
            value={fields.collapsibletext}
            onChange={(e) => handleFieldChange('collapsibletext', e.target.value)}
          />
        )}
      </div>

      <div className="numberBox">
        <h3>Temperature:</h3>
        <input
          type="text"
          value={fields.noncollapsibletext}
          onChange={(e) => handleFieldChange('noncollapsibletext', e.target.value)}
          placeholder="non-collapsible text"
        />
      </div>

      <div className="numberBox">
        <h3>Max tokens</h3>
        <input
          type="text"
          value={fields.noncollapsibletext}
          onChange={(e) => handleFieldChange('noncollapsibletext', e.target.value)}
          placeholder="non-collapsible text"
        />
      </div>

      <div>
        <label>checkbox</label>
        <input
          type="checkbox"
          checked={fields.isChecked}
          onChange={() => handleFieldChange('ischecked', !fields.isChecked)}
        />
      </div>
      <div className="collapsible-textbox">
      <label className="label">textbox</label>
      <div className="textbox-container">
        <input
          type="text"
          className={`textbox ${isCollapsed ? 'collapsed' : ''}`}
          placeholder="type here..."
        />
        <i
          className={`arrow-icon ${
            isCollapsed ? 'collapsed' : 'expanded'
          }`}
          onClick={toggleCollapse}
        >
          &#8595; {/* down arrow */}
        </i>
      </div>
    </div>
    </div>
  );
}

export default Settings;