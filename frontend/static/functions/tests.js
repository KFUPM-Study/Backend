const tests_list = document.getElementById("Tests-list")
const subject = window.location.href.split('/')
fetch(`http://127.0.0.1:8000/api/subjects/${subject[subject.length -1]}`)
.then(e => e.json())
.then(result =>{
    for(test of result){
        test_title = test.title
        test_picture = test.picture.slice(9)
        tests_list.innerHTML += `
        <div class="col-6 col-xl-4  mt-3">
            <div class="card" id="${test_title}">
                <img src="${test_picture}" class="card-img-top" alt="...">
                <div class="card-footer text-center">
                    ${test_title}
                </div>
            </div>
        </div>`
    }
})

tests_list.addEventListener('click', function(e){
    container = e.target.parentElement
    if(container.classList[0] === 'card'){
        window.location.href = `http://127.0.0.1:8000/test/${container.id}`
    }
})