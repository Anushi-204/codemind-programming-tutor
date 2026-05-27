async function explainConcept(){

let concept=document.getElementById("concept").value
let level=document.getElementById("level").value

let response=await fetch("/explain",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({concept,level})
})

let data=await response.json()

document.getElementById("output").innerText=data.result
}


async function generatePractice(){

let concept=document.getElementById("concept").value
let level=document.getElementById("level").value

let response=await fetch("/practice",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({concept,level})
})

let data=await response.json()

document.getElementById("output").innerText=data.result
}


async function generateTask(){

let concept=document.getElementById("concept").value
let level=document.getElementById("level").value

let response=await fetch("/task",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({concept,level})
})

let data=await response.json()

document.getElementById("output").innerText=data.result
}


async function generateRoadmap(){

let topic=document.getElementById("topic").value

let response=await fetch("/roadmap",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({topic})
})

let data=await response.json()

document.getElementById("roadmap").innerText=data.result
}


async function chat(){

let question=document.getElementById("question").value

let response=await fetch("/chat",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({question})
})

let data=await response.json()

document.getElementById("chat").innerText=data.result
}