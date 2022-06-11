
function changeActivePage(element, newClass) {
    element.classList.add(newClass)
}

const queryString = window.location.pathname.replace('/', '')
const _queryString = window.location.pathname.replace('/', '').replace('/', '-')

console.log(queryString)
if (_queryString.length === 0 ) {
    const queryString = 'home'
    const sideElement = document.querySelector('#'+queryString)
    changeActivePage(sideElement, 'active')

} else {
    console.log(_queryString)
    
    const sideElement = document.querySelector('#'+_queryString)
    changeActivePage(sideElement, 'active')
}
