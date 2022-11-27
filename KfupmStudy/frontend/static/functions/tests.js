const tests_list = document.getElementById("Tests-list")
const subject = window.location.href.slice(27)
console.log(subject)
fetch(`http://127.0.0.1:8000/api/subjects/${subject}`)
.then(e => e.json())
.then(result =>{
    for(test of result){
        test_title = test.title
        test_picture = test.picture.slice(8)
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

