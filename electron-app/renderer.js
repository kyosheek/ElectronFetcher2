// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.

console.log("binding functions");
document.getElementById("startButton").addEventListener("click", function() { retrieveData() }, false);
console.log("binded!");

const removeDivChilds = function() {
  const node = document.getElementById("retrievedData");
  while (node.firstChild) {
    node.removeChild(node.firstChild);
  }
}

const retrieveData = async function() {
  let url = document.getElementById("data").value;
  console.log("getting data from", url);
  let response = await fetch(url);
  console.log("response", response);
  let text = await response.text();
  console.log("response data:\n", text);
  let p = document.createElement("pre");
  p.innerText = text;
  removeDivChilds();

  document.getElementById("retrievedData").appendChild(p);
  setTimeout(() => {
    p.remove();
  }, 20000);
}
