import React from 'react';
import { File } from './File';
export const Folder = ({clickedFile, folder, handleElementClick, name}) => {
    return (
        <div key={`folder-${name}`}>
            <h3 key={`header-${name}`} onClick={handleElementClick(name, 0, 'folder')}>{name}</h3>
            <ul key={`ul-${name}`}>
                {
                    folder.map((str, fileIdx) => {
                        const isEmptyObj = Object.keys(clickedFile).length === 0;
                        const isClicked = !isEmptyObj && clickedFile.hasClicked && clickedFile.fileIdx === fileIdx ? true : false;

                        return (<File
                            key={fileIdx}
                            folderName={name}
                            handleElementClick={handleElementClick}
                            isClicked={isClicked}
                            index={fileIdx}
                            text={str}
                        />);
                    })
                }
            </ul>
        </div>
    );
}
