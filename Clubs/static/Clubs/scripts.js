const showModal = () => {
    let modalContainer = document.querySelector('#leaveClub')
    let leaveBtn = document.querySelector('.leaveBtn')
    if (modalContainer) {
        leaveBtn.addEventListener('click', evt => {
            // modalContainer.style.display = "block"
        })
    }
}

const hoverCircle = () => {
    let imgCircle = document.querySelector('.imgCircle')
    let circleOnHover = document.querySelector('.circleOnHover')
    if (imgCircle && circleOnHover) {
        imgCircle.addEventListener('mouseover', (evt) => {
            circleOnHover.classList.add('onHoverfilter')

        })

        imgCircle.addEventListener("mouseleave", (evt) => {
            circleOnHover.classList.remove('onHoverfilter')
        });
    }
}
const messageSuccess = () => {
    let savedWrap = document.querySelector('.savedWrap')
    if (savedWrap) {
        setTimeout(fade_out, 4200);

        function fade_out() {
            savedWrap.remove()
        }

    }
}
const areYouSure = () => {
    let areYouSureBTN = document.querySelector('.areYouSureBTN')
    let surePrompt = document.querySelector('.surePrompt')
    let cancelBtn = document.querySelector('.cancelBtn')
    if (areYouSureBTN) {
        [areYouSureBTN, cancelBtn].forEach(x => {
            x.addEventListener('click', evt => {
                areYouSureBTN.classList.toggle('d-none')
                surePrompt.classList.toggle('d-none')
            })
        })
    }
}
const formIcon = () => {
    let formIcon = document.querySelectorAll('.formIcon')
    if(formIcon){

        formIcon.forEach(icon =>{
            let iconInput = icon.querySelector('input')
            let textarea = icon.querySelector('textarea')

            if(textarea){iconInput=textarea}

            iconInput.addEventListener("focusin", function () {
                icon.querySelector('i').style.display = 'none'
            });
            iconInput.addEventListener("focusout", function () {
                icon.querySelector('i').style.display = 'block'
            });
                })
    }
}

allFunctions()
if (document.readyState !== 'loading') {
    allFunctions()
}

document.body.addEventListener('htmx:afterOnLoad', event => {
    allFunctions()
})

function allFunctions() {
    hoverCircle()
    messageSuccess()
    showModal()
    areYouSure()
     formIcon()
}
