async function checkNick(name) {
    const response = await fetch("https://codeforces.com/api/user.rating?handle=" + name);
    const data = await response.json();
    return data?.status == 'OK' ? true : false;
}


const modalForm = document.getElementById('formCheckUser');
const errorMsg = document.getElementById('error_msg');
modalForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorMsg.innerText = '';

    const data = new FormData(modalForm);

    const name_nick = data.get('name_nick');

    if (await checkNick(name_nick)) {
        modalForm.submit();
    }
    else {
        document.getElementById('error_msg').innerText = 'Такой пользователь не найден';
    }
})
