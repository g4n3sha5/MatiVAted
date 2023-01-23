const showNavbar = () => {
    const toggle = document.querySelector('#header-toggle'),
        nav = document.querySelector('#nav-bar'),
        navName = document.querySelectorAll('.nav_name'),
        myNavlist = document.querySelector('.nav_list'),
        closeNavIcon = document.querySelector('.closeNavIcon')

    if (toggle && nav && closeNavIcon ) {
        closeNavIcon.addEventListener('click', () =>  {
            toggleNav(nav, toggle, closeNavIcon, navName, myNavlist)
        })

        toggle.addEventListener('click', () => {
            // show navbar
            toggleNav(nav, toggle, closeNavIcon, navName, myNavlist)
        })
    }
}

const toggleNav = (nav, toggle, closeNavIcon, navName, myNavlist) =>{
    navName.forEach(el =>{
        console.log(getComputedStyle(el).opacity)
        if (getComputedStyle(el).opacity != 1 ){
            setTimeout(fade, 450);
            function fade() {
                el.classList.toggle('fade')
            }
        }
        else{
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
    if (techniqueItem.length > 0){ collection = techniqueItem }

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

/*===== LINK ACTIVE =====*/
const colorClick = () =>{
    const linkColor = document.querySelectorAll('.nav_link')
    if (linkColor) {
        linkColor.forEach(l => l.addEventListener('click', colorLink(linkColor)))
    }
}

function colorLink(linkColor){
    linkColor.forEach(l=> {
        l.classList.remove('active')

    })
     if(this.classList === undefined) {return}
    this.classList.add('active')
}

const chooseFile = (evt) => {
    document.querySelector('.imageInput').click()

}


allFunctionsMain()
if (document.readyState !== 'loading') {
    allFunctionsMain()
}

document.body.addEventListener('htmx:afterOnLoad', event=>{
    allFunctionsMain()
})
function allFunctionsMain(){
    searchItem()
    showNavbar()
    colorClick()
}
