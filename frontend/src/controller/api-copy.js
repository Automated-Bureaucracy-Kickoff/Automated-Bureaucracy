async function copyContent(data){
    await navigator.clipboard.writeText(data);

}



function handleFileSelection(event) {
  const file = event.target.files[0];

//   <div className="loading lv-circles sm lvl-5" data-label="Loading..." style={{display:"none"}}>
  // Read the file
  const reader = new FileReader();
  reader.onloadstart=()=>{
    document.querySelector(".loading").style.display="block"
  }
  reader.onload = () => {
    document.querySelector(".loading").style.display="none"
    dispatch(appendFiles({ files: event.target.files }))
  };

}


export {copyContent}