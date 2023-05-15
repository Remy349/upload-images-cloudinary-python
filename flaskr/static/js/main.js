document.addEventListener('DOMContentLoaded', () => {
  const notifications = document.getElementById('notifications')

  if (notifications) {
    const notificationCloseBtn = document.getElementById('notificationCloseBtn')

    notificationCloseBtn.addEventListener('click', () => {
      notifications.style.display = 'none'
    })
  }
})
