const subject_list = document.getElementById("subjects-list")
fetch('http://127.0.0.1:8000/api/subjects/')
.then(e => e.json())
.then(result =>{
    for(subject of result){
        sub_name = subject.name
        sub_picture = subject.picture.slice(10)
        subject_list.innerHTML += `
        <div class="col-6 col-sm-4 col-md-3 mt-3">
            <div class="card" id="${sub_name}">
                <img src="${sub_picture}" class="card-img-top" alt="...">
                <div class="card-footer text-center">
                    ${sub_name}
                </div>
            </div>
        </div>`
    }
})

subject_list.addEventListener('click', function(e){
    container = e.target.parentElement
    if(container.classList[0] === 'card'){
        window.location.href += `${container.id}`
    }
})