import React, { useEffect, useState } from 'react';
import update from 'immutability-helper';
import { useForm } from 'react-hook-form';
import { Folder } from './Folder';

export const Container = () => {
    // instantiate hook for the react-hook-form
    const { errors, handleSubmit, register, reset } = useForm();

    const [data, setData] = useState({});
    const [error, setError] = useState(false);
    const [dataLoaded, setDataLoaded] = useState(false);

    const [clickedFile, setClickedFile] = useState({hasClicked: false, folderName: '', fileIdx: 0});

    // handles click events on folders (h3 element) and files (li element)
    // wraps the function in a closure in order to save the parameters where they are defined
    // and handle both contexts used
    const handleElementClick = (folderName, fileIdx, elType) => () => {
        // adds the check to length > 0 to make sure that if create a new folder, it will not select an undefined element
        if (!clickedFile.hasClicked && data[folderName].length > 0) {
            setClickedFile({folderName: folderName, fileIdx: fileIdx, hasClicked: true});
        } 

        // uses another if instead of else to not try to append elements when we call this function without proper parameters (an undefined element)
        if (clickedFile.hasClicked){
            setClickedFile({folderName: '', fileIdx: 0, hasClicked: false});

            // do nothing if the folder and file are the same
            if (clickedFile.folderName === folderName && clickedFile.fileIdx === fileIdx) return; 

            setData(prevData => {
                // change type of data change based on which elType the event handler is being called from.
                // the result is if the elType is folder, just unshift the element to the top of the folder
                // if it is a file, actually splice it before the second index you clicked
                const fileToMove = prevData[clickedFile.folderName][clickedFile.fileIdx]; 

                // performs this update in two parts because of a bug that occurs when mixed together
                // when mixed, if the clickedFIle.folderName and the foldername name are the same, the splice
                // operations conflict with each other and duplicate the file in the same folder instead of removing it
                // splitting the update into two options creates another object in memory, but makes the code more readable
                const splicedData = update(prevData, {
                    [clickedFile.folderName]: { $splice: [[clickedFile.fileIdx, 1]] },
                });

                if (elType === 'folder') {
                    return update(splicedData, {
                        [folderName]: { $unshift: [fileToMove]}
                    });
                } else {
                    return update(splicedData, {
                        [folderName]: { $splice: [[fileIdx, 0, fileToMove]]}
                    });
                }
            })
        }

    }

    const onSubmit = (data, e) => {
        e.target.reset();
        reset();
        // uses the prevData to sort the previous data before operating on the new state
        setData(prevData => { 
            const unordered = {...prevData, [data.folderName]: []};
            const ordered = {}
            Object.keys(unordered).sort().forEach(key => {
                ordered[key] = unordered[key];
            });

            return ordered;
        });
    }

    // add effect to load in data before the app starts.
    // also sets an error if the loading wasn't able to be complete
    useEffect(() => {
        setDataLoaded(false);
        async function fetchData(url) {
            try {
                const response = await fetch(url);
                const json = await response.json()

                setDataLoaded(true);
                setData(json.data);
            } catch (e) {
                setError(true);
            }
        }

        fetchData('http://localhost:5000/files');

    }, []);

    return (
        <>
            {
                error && <div style={{color: `red`}}>some error occurred while fetching files</div>
            }

            {
                !dataLoaded ? <p>Loading...</p> : 
                    <>
                        <section style={{textAlign: 'left'}}>
                            <h3>Add a new folder!</h3>
                            <form onSubmit={handleSubmit(onSubmit)}>
                                { errors.folderName && <p style={{color: 'red'}}>The folderName is required to submit the form.</p>}
                                <input name="folderName" ref={register({ required: true })} />
                                <input type="submit" />
                            </form>
                        </section>
                        <section style={{ textAlign: "left" }}>
                            <h1>Folders</h1>

                            {Object.keys(data).map((folderName, index) => { 
                                // don't use destructuring because there would be a namespace clash
                                const doesFolderNameMatch = folderName === clickedFile.folderName;
                                return(<Folder 
                                    key={index} 
                                    clickedFile={doesFolderNameMatch ? clickedFile : {}}
                                    folder={data[folderName]} 
                                    handleElementClick={handleElementClick} 
                                    name={folderName} 
                                />);
                            })}
                        </section>
                    </>
            }
        </>
    );

}
