document.addEventListener('DOMContentLoaded', () => {
  const messageBtnClose = document.querySelector('.upload__message-icon')
  const message = document.querySelector('.upload__message')

  if (message) {
    messageBtnClose.addEventListener('click', () => {
      message.style.display = 'none'
    })
  }
})

