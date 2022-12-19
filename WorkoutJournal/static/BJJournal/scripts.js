//
// let addSession = document.getElementsByClassName ('addSession')
// if(addSession) {
//     addSession.forEach(sessionClass => {
//         console.log(sessionClass)
//         sessionClass.addEventListener('change', (evt) => {
//             evt.currentTarget
//                 .querySelectorAll('.activeType')
//                 .forEach(element => {
//                     element.classList.remove("activeType")
//                 })
//
//             evt.target
//                 .closest('.count_icon')
//                 .classList.add("activeType");
//         }, true);
//     })
// }
//

function onClickColor() {
    let addSession = document.getElementsByClassName('addSession')

    if (addSession) {

        Array.from(addSession).forEach(sessionClass => {
            Array.from(sessionClass.querySelectorAll('.count_icon'))
                .forEach(count_icon => {

                    count_icon.addEventListener('click', (evt) => {
                        sessionClass.querySelectorAll('.activeType')
                            .forEach(element => {
                                element.classList.remove("activeType")
                                })

                        evt.target
                            .closest('.count_icon')
                            .classList.add("activeType");
                    }, true);

                }, true);
        })
    }
}
function quickDateButtons() {
    let todayBtn = document.querySelector('.today')
    if (todayBtn) {

        let yesterdayBtn = document.querySelector('.yesterday')
        let datePicker = document.querySelector('.datepicker-input')
        let today = new Date()
        let yesterday = new Date(Date.now() - 86400000)


        todayBtn.addEventListener('click', (evt) => {
            datePicker.valueAsDate = today
        })

        yesterdayBtn.addEventListener('click', (evt) => {
            datePicker.valueAsDate = yesterday
        })
    }
}

function toggleActive(){
     let choiceButton = document.querySelectorAll('.choice-btn')
    let techniquesListWrap = document.querySelectorAll(('.techniquesListWrap'))
    if (choiceButton){
        let choiceArrowBtn = document.querySelectorAll(('.choiceArrowBtn'))

        choiceArrowBtn.forEach(btn =>
            {
                btn.addEventListener('click', (evt) => {

                    btn.classList.toggle('rotateButton')
                    document.querySelectorAll(('.techniquesListWrap')).forEach(elem => {

                        elem.classList.toggle('d-none')
                    })
            })

    })
    }
//TO BE FIXEDDDDDDDD
}

let filterList = searchTerm => {
    let optionsList = document.querySelectorAll('.techniqueOption')
    let techniqueItem = document.querySelectorAll('.techniqueItem')

    let collection = optionsList
    if (techniqueItem.length > 0){ collection=techniqueItem }

    searchTerm.toLowerCase()

    collection.forEach(option =>{
        let optionText = option.textContent.trim().toLowerCase()
        const textIncludes = optionText.includes(searchTerm)
        if (!option.classList.contains('cantSearch')){
            option.classList.toggle('d-none', !textIncludes)
        }

    })
}

function searchItem(){
    let searchBox = document.querySelector(('.searchBox'))
    if(searchBox) {
        searchBox.addEventListener('keyup', (evt) => {
            filterList(evt.target.value)

        })
    }
}

function multiSelect(){
    let techniqueList = document.querySelectorAll('.techniqueOption')
    let choicePlaceholder = document.querySelector('.choicePlaceholder')
    let choicePlaceholderWrapper = document.querySelector('.choicePlaceholderWrapper')

     techniqueList.forEach(technique =>{

        technique.addEventListener('click', (evt) =>{

            technique.classList.add('d-none', 'cantSearch')

            if (choicePlaceholder.textContent === "Choose techniques") choicePlaceholder.textContent = ''

            let TechniqueHTML = `<span data-element='${technique}'
                                        data-class='${technique.classList[0]}' 
                                        class='mb-1 chosenTechnique'>
             
                        ${technique.textContent.trim()}   
                        <i class="pe-none bi bi-x-octagon" ></i>
          
                    </span>`

            choicePlaceholderWrapper.insertAdjacentHTML("beforeend", TechniqueHTML)
            removeToggle(choicePlaceholderWrapper, choicePlaceholder)

        })


    })

}
function removeToggle(choicePlaceholderWrapper, choicePlaceholder){
    let removeIcon = document.querySelectorAll('.chosenTechnique')
    let techniquesOptions = document.querySelector('.techniquesOptions')
    removeIcon.forEach(icon =>{
        icon.addEventListener('click', (evt) =>{
            let sortAttribute = icon.getAttribute('data-class')
            let elementToView = document.querySelector(`.${sortAttribute}`)
            elementToView.classList.remove('d-none', 'cantSearch')
            evt.target.remove()
            if (choicePlaceholderWrapper.textContent.trim() === '') choicePlaceholder.textContent = "Choose techniques"

        })


    })
    // if (choicePlaceholder.textContent === '') choicePlaceholder.textContent = "Choose techniques"

}

function editDescription(){
    let editButton = document.querySelector('.editButton')
    let addButton = document.querySelector('.addButton')
    let techDescription = document.querySelector('.techDescription')
    let suggestBtn = document.querySelector('.suggestBtn')
    let techDescriptionInput = document.querySelector('.techDescriptionInput')

    if (editButton){
        editButton.addEventListener('click', (evt) =>{
            addButton.classList.toggle('d-none')
            let descriptionHeight = techDescription.clientHeight
            editButton.classList.toggle('editing')
            showDescription(techDescription, techDescriptionInput, suggestBtn)
            techDescriptionInput.style.maxHeight = descriptionHeight + "px"
            techDescriptionInput.querySelector('textarea').value = techDescription.textContent.trim()
    })
}
    if(addButton){
        addButton.addEventListener('click', (evt) =>{
            showDescription(techDescription, techDescriptionInput, suggestBtn)
            techDescriptionInput.style.height = 50 + '%'
        })

    }
}


const showDescription = (techDesc, techInput, suggestBtn) =>{
    if(techDesc){
        techDesc.classList.toggle('d-none')
    }
    if (techInput){
        techInput.classList.toggle('d-none')
        techInput.classList.toggle('d-flex')
    }
    if(suggestBtn){
       suggestBtn.classList.toggle('d-none')
    }

}



if (document.readyState !== 'loading') {
    allFunctions()
}
document.body.addEventListener('htmx:afterOnLoad', event=>{
    allFunctions()
})


function allFunctions(){
     multiSelect()
    onClickColor()
    quickDateButtons()
    toggleActive()
    searchItem()
    editDescription()


}