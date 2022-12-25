let userNameInput = document.querySelector('#userName');
let visibilityUserNameBtn = document.querySelector('#visibilityName');
let eyeIcon = visibilityUserNameBtn.querySelector('i');
let authBtn = document.querySelector('#authUser');
let formAuth = document.querySelector('#authUsersForm');

function visibilityName() {
    if (userNameInput.getAttribute('type') === 'text') {
        eyeIcon.classList.remove('bi-eye');
        eyeIcon.classList.add('bi-eye-slash');
        userNameInput.setAttribute('type', 'password');
    } else {
        eyeIcon.classList.remove('bi-eye-slash');
        eyeIcon.classList.add('bi-eye');
        userNameInput.setAttribute('type', 'text');
    }
}

eyeIcon.addEventListener('click', () => {
    visibilityName();
});
