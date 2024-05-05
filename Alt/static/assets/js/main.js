let logoutLink = document.getElementById('logout-link');

logoutLink.addEventListener('click', async (event) =>
{
    let message = 'Вы собираетесь выйти из аккаунта.';

    if (!confirm(message))
    {
        event.preventDefault();
    }
});