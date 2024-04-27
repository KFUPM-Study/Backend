const title = document.getElementById('title')
const container = document.getElementById('questions')

function main(){
    getTest()
}
async function getTest(){
    fetch(`http://127.0.0.1:8000/api/tests/${title.innerHTML}`)
    .then(e => e.json())
    .then(result =>{
        //console.log(result.questions)
        for(question of result.questions){
            let data = `
            <div class="card">
                <div class="card-header">
                    ${question.question_body}
                </div>
                <div class='card-body'>
                    <select class="form-select" aria-label="Default select example" id='${question.id}'>
            `
            for(choice of question.choices){
                data += `<option value="${choice.id}">${choice.choice_body}</option>`
            }

            data += "</select></div>"
            container.innerHTML += data
        }
        container.innerHTML += '<button type="button" class="btn btn-success mt-2" id="submit_btn">Submit</button>'
    })    

}

function submitTest(){
    console.log("hello")
}

main()