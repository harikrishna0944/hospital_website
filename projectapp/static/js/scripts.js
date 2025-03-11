document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const modal = document.getElementById('loginModal');
    const closeModal = document.getElementById('closeModal');

    // Show Modal
    loginBtn.addEventListener('click', () => {
        modal.style.display = 'flex';
        modal.setAttribute('aria-hidden', 'false');
    });

    // Close Modal
    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
        modal.setAttribute('aria-hidden', 'true');
    });

    // Close Modal When Clicking Outside Content
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
            modal.setAttribute('aria-hidden', 'true');
        }
    });
});
