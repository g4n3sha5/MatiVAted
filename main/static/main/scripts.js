const showNavbar = () => {
    const toggle = document.querySelector('#header-toggle'),
        nav = document.querySelector('#nav-bar'),
        navName = document.querySelectorAll('.nav_name'),
        myNavlist = document.querySelector('.nav_list'),
        closeNavIcon = document.querySelector('.closeNavIcon')

    if (toggle && nav && closeNavIcon) {
        closeNavIcon.addEventListener('click', () => {
            toggleNav(nav, toggle, closeNavIcon, navName, myNavlist)

        })

        toggle.addEventListener('click', () => {
            // show navbar

            toggleNav(nav, toggle, closeNavIcon, navName, myNavlist)
        })
    }
}

const toggleNav = (nav, toggle, closeNavIcon, navName, myNavlist) => {
    navName.forEach(el => {

        if (getComputedStyle(el).opacity != 1) {
            setTimeout(fade, 450);

            function fade() {
                el.classList.toggle('fade')
            }
        } else {
            el.classList.toggle('fade')
        }

        // el.classList.toggle('d-none')

    })
    let header_toggle = document.querySelector('.header_toggle')
    nav.classList.toggle('show')
    toggle.classList.toggle('d-none')
    header_toggle.classList.toggle('text-center')
    header_toggle.classList.toggle('text-end')
    closeNavIcon.classList.toggle('d-none')
    myNavlist.classList.toggle('align-items-center')


}


let filterList = searchTerm => {
    let optionsList = document.querySelectorAll('.techniqueOption')
    let techniqueItem = document.querySelectorAll('.techniqueItem')

    let collection = optionsList
    if (techniqueItem.length > 0) {
        collection = techniqueItem
    }

    searchTerm.toLowerCase()

    collection.forEach(option => {
        let optionText = option.textContent.trim().toLowerCase()
        const textIncludes = optionText.includes(searchTerm)
        if (!option.classList.contains('cantSearch')) {
            option.classList.toggle('d-none', !textIncludes)
        }

    })
}

function searchItem() {
    let searchBox = document.querySelector(('.searchBox'))
    if (searchBox) {
        searchBox.addEventListener('keyup', (evt) => {
            filterList(evt.target.value)

        })
    }
}

/*===== LINK ACTIVE =====*/
const colorClick = () => {
    const linkColor = document.querySelectorAll('.nav_link')
    if (linkColor) {
        linkColor.forEach(l => l.addEventListener('click', colorLink(linkColor)))
    }
}

function colorLink(linkColor) {
    linkColor.forEach(l => {
        l.classList.remove('active')

    })
    if (this.classList === undefined) {
        return
    }
    this.classList.add('active')
}


const formIcon = () => {
    let formIcon = document.querySelectorAll('.formIcon')
    if (formIcon) {

        formIcon.forEach(icon => {
            let iconInput = icon.querySelector('input')
            let textarea = icon.querySelector('textarea')

            if (textarea) {
                iconInput = textarea
            }

            iconInput.addEventListener("focusin", function () {
                icon.querySelector('i').style.display = 'none'
            });
            iconInput.addEventListener("focusout", function () {
                icon.querySelector('i').style.display = 'block'
            });
        })
    }
}
const zeroCheck = (digit) => {
    let x = digit.toString()
    if (x.length === 1) {
        x = '0' + digit.toString()
    }
    return x
}

function quickTimeButtons() {
    let quickTimeBtn = document.querySelectorAll('.quickTimeBtn')
    let timeStampBtn = document.querySelectorAll('.timeStampBtn')
    let timeInput = document.querySelector('.timeLabel input')
    if (quickTimeBtn) {
        quickTimeBtn.forEach(btn => {
            let btnValue = btn.textContent
            if (btnValue.length === 4) {
                btnValue = '0' + btnValue
            }
            btn.addEventListener('click', (evt) => {
                timeInput.value = btnValue
            })
        })
    }

    if (timeStampBtn) {
        timeStampBtn.forEach(btn => {
            btn.addEventListener('click', evt => {
                let minus = btn.querySelector('.bi-dash')
                let timeStampValue = btn.textContent
                let time = timeInput.value
                if (!time) {
                    time = '00:00'
                }
                let hours = time.slice(0, -3)
                let minutes = time.slice(-2)

                if (timeStampValue.includes('h')) {
                    if (minus) {
                        hours = parseInt(hours) - parseInt(timeStampValue)
                    } else {
                        hours = parseInt(hours) + parseInt(timeStampValue)
                    }

                }
                if (timeStampValue.includes('min')) {
                    minutes = parseInt(minutes) + parseInt(timeStampValue)

                    if (minutes >= 60) {
                        let hoursLeft = Math.floor(minutes / 60)
                        let minutesLeft = minutes % 60
                        hours = parseInt(hours) + hoursLeft

                        minutes = minutesLeft
                    }
                }
                hours = zeroCheck(hours)
                minutes = zeroCheck(minutes)
                timeInput.value = hours + ':' + minutes
            })

        })
    }
}

const leftNavPadding = () => {
    const leftNav = document.querySelector('.l-navbar')
    if (leftNav) {
        document.querySelector('#footer').classList.add('leftNavPadding')
    }
}
const navOnHover = () => {
    const dropParent = document.querySelectorAll('.dropdownParent')
    dropParent.forEach(elem => {
         let dropdown =   elem.querySelector('.navDropdown')
        elem.addEventListener('mouseover', (evt) => {
          dropdown.style.display = "block"
        })

        elem.addEventListener('mouseleave', () => {
           dropdown.style.display = "none"
        })
    })
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


allFunctionsMain()
if (document.readyState !== 'loading') {
    allFunctionsMain()
}

document.body.addEventListener('htmx:afterOnLoad', event => {
    searchItem()
    quickTimeButtons()
    leftNavPadding()
    // allFunctionsMain()
})


function allFunctionsMain() {

     areYouSure()
    navOnHover()
    quickTimeButtons()
    searchItem()

    showNavbar()
    colorClick()
    formIcon()
    leftNavPadding()
}
