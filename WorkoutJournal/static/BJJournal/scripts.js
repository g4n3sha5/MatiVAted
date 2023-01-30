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

function toggleActive() {
    let choiceButton = document.querySelector('.choice-btn')
    if (choiceButton) {
        let choiceArrowBtn = document.querySelector(('.choiceArrowBtn'))
        choiceArrowBtn.addEventListener('click', (evt) => {
            choiceArrowBtn.classList.toggle('rotateButton')
        })

    }
}


function multiSelect(){
    // let techniqueList = document.querySelectorAll('.techniqueOption')
    let techniqueOption = document.querySelectorAll('.techniqueOption')
    let choicePlaceholder = document.querySelector('.choicePlaceholder')
    let choicePlaceholderWrapper = document.querySelector('.choicePlaceholderWrapper')

     techniqueOption.forEach(technique =>{
        technique.addEventListener('click', (evt) =>{
            evt.preventDefault()
            let checkBox = technique.querySelector('input')
            checkBox.checked=true
            technique.classList.add('d-none', 'cantSearch')

            if (choicePlaceholder.textContent === "Choose techniques") choicePlaceholder.textContent = ''

            let TechniqueHTML = `<span   
                                    data-class='${technique.classList[0]}' 
                                    class='mb-1 chosenTechnique'>
                        ${technique.textContent.trim()}   
                        <i class="pe-none bi bi-x-octagon" ></i>
      
                    </span>`

            choicePlaceholderWrapper.insertAdjacentHTML("beforeend", TechniqueHTML)

            removeToggle(choicePlaceholderWrapper, choicePlaceholder, checkBox)


        })


    })

}

function removeToggle(choicePlaceholderWrapper, choicePlaceholder, checkBox=false){

    let removeIcon = document.querySelectorAll('.chosenTechnique')
    let techniquesOptions = document.querySelector('.techniquesOptions')

    removeIcon.forEach(icon =>{
        icon.addEventListener('click', (evt) =>{
            console.log("remove", checkBox.checked)
            let sortAttribute = icon.getAttribute('data-class')
            let elementToView = document.querySelector(`.${sortAttribute}`)
            elementToView.classList.remove('d-none', 'cantSearch')
            evt.target.remove()
            checkBox.checked = false
            if (choicePlaceholderWrapper.textContent.trim() === '') choicePlaceholder.textContent = "Choose techniques"

        })


    })
    // if (choicePlaceholder.textContent === '') choicePlaceholder.textContent = "Choose techniques"

}

function editDescription(){
    let editButton = document.querySelectorAll('.editButton')
    let addButton = document.querySelector('.addButton')
    let techDescription = document.querySelector('.techDescription')
    let suggestBtn = document.querySelector('.suggestBtn')
    let techDescriptionInput = document.querySelector('.techDescriptionInput')

    if (editButton){
        Array.from(editButton).forEach(btn => {
            btn.addEventListener('click', (evt) =>
            {
                // let addButton = btn.parentNode.parentNode.querySelector('.addButton')
                if(addButton){
                    addButton.classList.toggle('d-none')
                }

                let descriptionHeight = techDescription.clientHeight
                btn.classList.toggle('editing'
                )
                techDescriptionInput.style.maxHeight = descriptionHeight + "px"
                techDescriptionInput.querySelector('textarea').value = techDescription.textContent.trim()
                if(suggestBtn) { showDescription(techDescription, techDescriptionInput, suggestBtn)}
                else { showDescription(techDescription, techDescriptionInput)}

            })
        })
    }

    if(addButton){
         Array.from(addButton).forEach(btn => {
             btn.addEventListener('click', (evt) => {
                 let techDescriptionInput = btn.parentNode.querySelector('.techDescriptionInput')
                 let techDescription = btn.parentNode.querySelector('.techDescription')

                 if(suggestBtn){ showDescription(techDescription, techDescriptionInput, suggestBtn)}
                 else{ showDescription(techDescription, techDescriptionInput)}

                 techDescriptionInput.style.height = 30 + '%'

             })
         })
    }
}

const showDescription = (techDesc, techInput, suggestBtn = false) =>{
    if(techDesc){
        techDesc.classList.toggle('d-none')
    }
    if (techInput){
        // techInput.classList.toggle('d-none')
        techInput.classList.toggle('d-flex')
    }
    if(suggestBtn){
       suggestBtn.classList.toggle('d-none')
    }

}

const showModal = () => {
    let modalContainer = document.querySelector('#modalContainer')
    let yourSessionsSection = document.querySelector('.yourSessionsSection')
    if (yourSessionsSection){
        yourSessionsSection.addEventListener('htmx:afterOnLoad', evt=>{
        if (evt.detail.target.id === "modalContainer") {
            modalContainer.style.display = "block"
        }
    })
    }
}

const closeModal = () => {

    let container = document.querySelector('#modalContainer')
	let backdrop = document.querySelector('#modal-backdrop')
	let modal = document.querySelector('#MajModal')
    if(container){
	container.style.display = "None"
        }
	backdrop.classList.remove("show")

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
    showModal()
}