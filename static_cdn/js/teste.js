document.getElementById('açao').addEventListener('click', function (notificar) {
  notificar.preventDefault()

  alert('Essa opção está em manutenção aguarde')
})

document
  .getElementById('açao1')
  .addEventListener('click', function (notificar1) {
    notificar1.preventDefault()

    alert('Essa opção está em manutenção aguarde')
  })

function menuShow() {
  let menumobile = document.querySelector('.mobile-menu')
  if (menumobile.classList.contains('open')) {
    menumobile.classList.remove('open')
    document.querySelector('.icon').src = 'icon/menu_white_36dp.svg'
  } else {
    menumobile.classList.add('open')
    document.querySelector('.icon').src = 'icon/close_white_36dp.svg'
  }
}
