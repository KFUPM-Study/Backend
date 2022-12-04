const title = document.getElementById('title')
const container = document.getElementById('questions')
fetch(`http://127.0.0.1:8000/api/tests/${title.innerHTML}`)
.then(e => e.json())
.then(result =>{
    //console.log(result.questions)
    for(question of result.questions){
        let data = `
        <h1>${question.question_body}</h1>
        <ul>
            <li>${question.answers.choice_A}</li>
            <li>${question.answers.choice_B}</li>
            <li>${question.answers.choice_C}</li>
            <li>${question.answers.choice_D}</li>
        </ul>
        `
        container.innerHTML += data
    }  
})