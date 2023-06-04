
const signInEl = document.querySelector('.button_sign')
const signUpEl = document.querySelector('.button_signup')
const siginboxEl = document.querySelector('#siginbox')
const sigupboxEl = document.querySelector('#sigupbox')
const burgerEl = document.querySelector('.burger')
const mainPageEl = document.querySelector('.main-page')
const headerEl = document.getElementById('header')

const navbarButtonEl = document.getElementById('navButton')
const navbarEl = document.querySelector('.navbar')

const initApp = () => {
  navButtonElements()
  headerButtonElements()
  createArticles()
}

document.addEventListener('DOMContentLoaded', initApp())


function navButtonElements(){
  const navIcons = ['far', 'far', 'fas']
  const navIconClass = ['fa-bookmark', 'fa-paper-plane', 'fa-search']
  for(let i = 0; i < 3; i++){
    const button = document.createElement('i')
    button.classList.add(navIcons[i])
    button.id = navIconClass[i]
    button.classList.add(navIconClass[i])
    navbarButtonEl.prepend(button)
  }
}

function headerButtonElements(){
  const headerButtons = ['latest', 'home', 'news', 'politics', 'health', 'music']
  for(let i = 0; i < headerButtons.length; i++){
    const button = document.createElement('button')
    button.innerText = headerButtons[i]
    headerEl.prepend(button)
  }
}

function createArticles(){
  const buttonIcons = ['fas', 'fas']
  const buttonIconClass = ['fa-heart', 'fa-eye']
  const iconClass = ['heart', 'eye']

  for(let i = 0; i < 10; i++){
    const articleEl = document.createElement('article')
    const divImage = document.createElement('div')
    const imageEl = document.createElement('img')
    const lowerDiv = document.createElement('div')
    const container = document.createElement('div')
    const profileDiv = document.createElement('div')
    const profilePic = document.createElement('img')
    const authorName = document.createElement('p')
    const reactionsDiv = document.createElement('div')

    reactionsDiv.classList.add('reactions')

    let reactionsIcon;
    let iconCount;
    for(let i = 0; i < 2; i++){
      reactionsIcon = document.createElement('span')
      iconCount = document.createElement('span')

      reactionsIcon.classList.add(buttonIcons[i])
      reactionsIcon.classList.add(buttonIconClass[i])
      iconCount.classList.add('count')
      iconCount.classList.add(iconClass[i])
      iconCount.textContent = 0
      reactionsIcon.append(iconCount)
      reactionsDiv.append(reactionsIcon)
    }

    articleEl.classList.add('hot-block')
    divImage.classList.add('image-block')
    lowerDiv.classList.add('bottom')
    container.classList.add('autor')
    profileDiv.classList.add('profile-picture')
    authorName.textContent = 'author'

    divImage.append(imageEl)
    profileDiv.append(profilePic)
    container.append(profileDiv)
    container.appendChild(authorName)
    lowerDiv.append(container)
    lowerDiv.appendChild(reactionsDiv)

    articleEl.append(divImage)
    articleEl.appendChild(lowerDiv)
    articleEl.appendChild(reactionsDiv)

    mainPageEl.append(articleEl)
  }
}

const searchbuttonEl = document.getElementById('fa-search')
const searchboxEl = document.querySelector('.search-box')

// function listeners(){
  signInEl.addEventListener('click', () => {
    siginboxEl.style.display = siginboxEl.style.display === 'none' ? 'block' : 'none'
    sigupboxEl.style.display= 'none'
    searchboxEl.style.display = 'none'
    
  })

  signUpEl.addEventListener('click', () => {
    sigupboxEl.style.display = sigupboxEl.style.display === 'none' ? 'block' : 'none'
    siginboxEl.style.display = 'none'
    searchboxEl.style.display = 'none'
  })

  searchbuttonEl.addEventListener('click', () => {
    searchboxEl.style.display = searchboxEl.style.display === 'none' ? 'block' : 'none'
    siginboxEl.style.display = 'none'
    sigupboxEl.style.display= 'none'
  })

  burgerEl.addEventListener('click', () => {
    headerEl.classList.toggle('show')
    burgerEl.classList.toggle('show-color')
  })
