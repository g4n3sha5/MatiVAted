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

const chooseFile = (evt) => {
    document.querySelector('.imageInput').click()

}

const hoverCircle = () =>{
    let imgCircle = document.querySelector('.imgCircle')
    let circleOnHover = document.querySelector('.circleOnHover')
    imgCircle.addEventListener('mouseover', (evt) =>{
        circleOnHover.classList.add('onHoverfilter')

    })

    imgCircle.addEventListener("mouseleave", (evt) => {
        circleOnHover.classList.remove('onHoverfilter')
  });
}
const messageSuccess = () =>{
      let savedWrap = document.querySelector('.savedWrap')
    if (savedWrap){
        setTimeout(fade_out, 3000);
    function fade_out() {
        savedWrap.remove()
    }

    }
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

allFunctions()
if (document.readyState !== 'loading') {
    allFunctions()
}

document.body.addEventListener('htmx:afterOnLoad', event=>{
    allFunctions()
})


function allFunctions(){
    searchItem()
    hoverCircle()
    messageSuccess()
}