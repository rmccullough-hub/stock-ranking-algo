import React, {useState, useEffect, useCallback} from 'react';

function Popup() {
    const [show, setShow] = useState(true)

    return (
    <div className="bg">
      <div className="modal">
        <button id="close-btn" className="close-btn" onClick={()=>{
          return null
        }}>+</button>
      </div>
    </div>
    );
      
}

export default Popup;