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

/*
function responsiveBackend() {
    const smallScreens = window.matchMedia('(max-width: 768px)')
    const bigScreens = window.matchMedia('(min-width: 768px)')
    // const BJRview = document.querySelector('#BJR_view')
    let xhttp = new XMLHttpRequest();
    let screen = false
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    if (smallScreens.matches) {
        screen = 'small'
    }
    if (bigScreens.matches) {
        screen = 'big'
    }

    fetch('/yourSessions/', {
        method: 'POST',
        headers: {
            'contentType': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': token,
        },
        body: JSON.stringify({'device': screen})

    })
*/

// .then(response => response.json())

// $.ajax({
//     url: "/yourSessions/",
//     type:"POST",
//     data: {
//         'X-CSRFToken': token,
//         'screen' : screen
//     },
//     dataType: "json",
//
// })


// }

function onClickColor() {
    const addSession = document.querySelector('.addSessionSection')
    const count_icon = document.querySelectorAll('.count_icon')
    // let lengthTYPE = document.querySelector('.lengthTYPE')

    if (count_icon) {
        Array.from(count_icon)

            .forEach(count_icon => {
                let checkbox = count_icon.querySelector('input[type=radio]')
                if (checkbox) {
                    if (checkbox.checked) {
                        count_icon.classList.add("activeType");
                    }
                }

                count_icon.addEventListener('click', (evt) => {
                    let parent = count_icon.parentNode
                    if (parent.classList.contains('countWrap')) {
                        parent = count_icon.parentNode.parentNode
                    }
                    parent.querySelectorAll('.activeType')
                        .forEach(element => {
                            element.classList.remove("activeType")
                        })

                    evt.target
                        .closest('.count_icon')
                        .classList.add("activeType");
                }, true);

            }, true);
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
    let techniquesListWrap = document.querySelector('.techniquesListWrap')

    if (choiceButton) {
        let choiceArrowBtn = document.querySelector(('.choiceArrowBtn'))
        choiceArrowBtn.addEventListener('click', (evt) => {
            choiceArrowBtn.classList.toggle('rotateButton')
            if (techniquesListWrap.parentNode.classList.contains('userSuggestions')) {
                techniquesListWrap.classList.toggle('d-none')
            }


        })

    }
}


function multiSelect() {

    // let techniqueList = document.querySelectorAll('.techniqueOption')
    let techniqueOption = document.querySelectorAll('.techniqueOption')
    let choicePlaceholder = document.querySelector('.choicePlaceholder')
    let choicePlaceholderWrapper = document.querySelector('.choicePlaceholderWrapper')

    techniqueOption.forEach(technique => {
        let checkBox = technique.querySelector('input')
        let TechniqueHTML = `<span   
                                    data-class='${technique.classList[0]}' 
                                    class='mb-1 chosenTechnique'>
                        ${technique.textContent.trim()}   
                        <i class="pe-none bi bi-x-octagon" ></i>
      
                    </span>`

        if (checkBox.checked) {

            // technique.classList.add('d-none', 'cantSearch')
            if (choicePlaceholder.textContent === "Choose techniques") choicePlaceholder.textContent = ''
            choicePlaceholderWrapper.insertAdjacentHTML("beforeend", TechniqueHTML)
            // removeToggle(choicePlaceholderWrapper, choicePlaceholder, technique)

        }
        technique.addEventListener('click', (evt) => {
            evt.preventDefault()
            technique.querySelector('input').checked = true
            // console.log()
            // technique.classList.add('d-none', 'cantSearch')

            if (choicePlaceholder.textContent === "Choose techniques") choicePlaceholder.textContent = ''
            choicePlaceholderWrapper.insertAdjacentHTML("beforeend", TechniqueHTML)
            removeToggle(choicePlaceholderWrapper, choicePlaceholder)
            // removeToggle(choicePlaceholderWrapper, choicePlaceholder, technique)

        })

    })
     removeToggle(choicePlaceholderWrapper, choicePlaceholder)

}

function removeToggle(choicePlaceholderWrapper, choicePlaceholder, technique=false) {

    let removeIcon = document.querySelectorAll('.chosenTechnique')
    // let techniquesOptions = document.querySelector('.techniquesOptions')

    removeIcon.forEach(icon => {

        icon.addEventListener('click', (evt) => {
            evt.stopPropagation()
            let sortAttribute = icon.getAttribute('data-class')
            let elementToView = document.querySelector(`.${sortAttribute}`)
            elementToView.classList.remove('d-none', 'cantSearch')
            evt.target.remove()
            elementToView.querySelector('input').checked = false
            // checkBox.checked = false
            if (choicePlaceholderWrapper.textContent.trim() === '') choicePlaceholder.textContent = "Choose techniques"

        })


    })
    // if (choicePlaceholder.textContent === '') choicePlaceholder.textContent = "Choose techniques"

}

function editDescription() {
    let editButton = document.querySelectorAll('.editButton')
    let addButton = document.querySelector('.addButton')
    let techDescription = document.querySelector('.techDescription')
    let suggestBtn = document.querySelector('.suggestBtn')
    let techDescriptionInput = document.querySelector('.techDescriptionInput')

    if (editButton) {
        Array.from(editButton).forEach(btn => {
            btn.addEventListener('click', (evt) => {
                // let addButton = btn.parentNode.parentNode.querySelector('.addButton')
                if (addButton) {
                    addButton.classList.toggle('d-none')
                }

                let descriptionHeight = techDescription.clientHeight
                btn.classList.toggle('editing'
                )
                // techDescriptionInput.style.transform = `scaleX(100% + ${descriptionHeight} + px)`
                techDescriptionInput.style.maxHeight = descriptionHeight + "px"
                techDescriptionInput.querySelector('textarea').value = techDescription.textContent.trim()
                if (suggestBtn) {
                    showDescription(techDescription, techDescriptionInput, suggestBtn)
                } else {
                    showDescription(techDescription, techDescriptionInput)
                }

            })
        })
    }

    if (addButton) {
        addButton.addEventListener('click', (evt) => {
            let techDescriptionInput = addButton.parentNode.querySelector('.techDescriptionInput')
            let techDescription = addButton.parentNode.querySelector('.techDescription')

            if (suggestBtn) {
                showDescription(techDescription, techDescriptionInput, suggestBtn)
            } else {
                showDescription(techDescription, techDescriptionInput)
            }

            // techDescriptionInput.style.height = 30 + '%'

        })
    }
}

const showDescription = (techDesc, techInput, suggestBtn = false) => {

    if (techDesc) {
        techDesc.classList.toggle('d-none')
    }
    if (techInput) {
        let wrapp = document.querySelector('.techDescriptionWrap')
        // techInput.classList.toggle('d-none')
        techInput.classList.toggle('d-flex')


    }
    if (suggestBtn) {
        suggestBtn.classList.toggle('d-none')
    }

}

const showModal = () => {
    let modalContainer = document.querySelector('#modalContainer')
    let yourSessionsSection = document.querySelector('.yourSessionsSection')
    if (yourSessionsSection) {
        yourSessionsSection.addEventListener('htmx:afterOnLoad', evt => {
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
    if (container) {
        container.style.display = "None"
    }
    backdrop.classList.remove("show")

}

function quickFightTimeButtons() {
    let fightTime = document.querySelector('.fightTime')
    let fightTimeInput = document.querySelector('.fightTimeInput')
    let plusWrap = document.querySelector('.plusWrap')
    let minusWrap = document.querySelector('.minusWrap')

    if (fightTime) {

        plusWrap.addEventListener('click', evt => {
            fightTimeInput.stepUp()
        })
        minusWrap.addEventListener('click', evt => {
            fightTimeInput.stepDown()
        })
        for (let x of Array(41).keys()) {
            if (x % 5 === 0) {
                let html = ` <div class="count_icon addSessionLength cursor-pointer addSessionFight text-center">
                    <div class=" py-1">
                        <h3 class="m-0">
                            ${x}
                            <h4 class="m-0 smallCapt">min</h4>
                        </h3>
                    </div>
            </div>`;

                fightTime.insertAdjacentHTML('beforeend', html)
                fightTime.lastChild.addEventListener('click', evt => {
                    // evt.target.classList.o
                    fightTimeInput.value = x
                })
            }
        }
    }
}

const populateInput = () => {
    let sessionLocation = document.querySelector('.sessionLocation')
    if (sessionLocation) {
        let vari = sessionLocation.getAttribute('data-club')
        sessionLocation.querySelector('input').value = vari
    }
}

if (document.readyState !== 'loading') {
    allFunctions()
}

document.body.addEventListener('htmx:afterOnLoad', event => {
    allFunctions()

})


function allFunctions() {
    multiSelect()
    onClickColor()
    quickDateButtons()
    editDescription()
    showModal()
    toggleActive()
    quickFightTimeButtons()
    populateInput()

}