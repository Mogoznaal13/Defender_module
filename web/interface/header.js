function authIsAdmin() {
    let user = JSON.parse(sessionStorage.getItem('user'));
    return user.role === 'admin';
}

function adminSectionsRender() {
    const usersManageSectionBtn = document.querySelector('#usersManageSection');
    const logSection = document.querySelector('#logSection');

    if (authIsAdmin()) {
        usersManageSectionBtn.classList.add('visible');
        logSection.classList.add('visible');

        usersManageSectionBtn.classList.remove('invisible');
        logSection.classList.remove('invisible');
    } else {
        usersManageSectionBtn.classList.add('invisible');
        logSection.classList.add('invisible');

        usersManageSectionBtn.classList.remove('visible');
        logSection.classList.remove('visible');
    }
}

adminSectionsRender();
