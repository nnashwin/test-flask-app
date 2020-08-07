import React, { useState } from 'react';

export const File = ({folderName, text, handleElementClick, index, isClicked}) => {
    const highlightStyle = {
        backgroundColor: 'black',
        color: 'whitesmoke'
    };

    return (
        <>
            <li 
                key={index} 
                onClick={handleElementClick(folderName, index, 'file')} 
                style={isClicked ? highlightStyle : {}}
                value={'file'}>{text}</li>
        </>
    );
}
