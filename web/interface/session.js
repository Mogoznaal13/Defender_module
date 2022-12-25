let logoutBtn = document.querySelector('#logoutBtn');

function isAuth() {
    let user = JSON.parse(sessionStorage.getItem('user'));
    return user.auth_status;
}

function logout() {
    let user = JSON.parse(sessionStorage.getItem('user'));
    sessionStorage.removeItem('user');
    window.location.replace('../pages/auth.html');
    eel.logWrite(`Пользователь ${user.name} вышел из системы!`, 'warning');

    return
}

document.addEventListener('load', () => {
    if (!isAuth()) {
        window.location.replace('auth.html');
    }
});

logoutBtn.addEventListener('click', () => {
    logout();
});
