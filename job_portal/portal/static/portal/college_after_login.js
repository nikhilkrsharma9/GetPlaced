// Handles AJAX ticket raising for college dashboard
function raiseTicketAJAX(collegeId, companyId, jobId, btn) {
    btn.disabled = true;
    btn.textContent = 'Raising...';
    // Find the CSRF token from the form (not from document, for correct token)
    let form = btn.closest('form');
    let csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch('/raise_ticket/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: `college_id=${collegeId}&company_id=${companyId}`
    })
    .then(response => response.json())
    .then(data => {
        btn.textContent = 'Ticket Raised';
        btn.style.background = data.success ? '#43cea2' : '#b7e4c7';
        btn.style.color = '#155724';
        btn.disabled = true;
        // Remove any existing Go to Chat button next to this button
        let next = btn.nextElementSibling;
        if (next && next.classList.contains('go-to-chat-btn')) {
            next.remove();
        }
        if (data.chat_url) {
            const chatBtn = document.createElement('a');
            chatBtn.href = data.chat_url;
            chatBtn.textContent = 'Go to Chat';
            chatBtn.className = 'go-to-chat-btn';
            chatBtn.style = 'background:#1976d2;color:#fff;padding:4px 12px;border-radius:3px;text-decoration:none;margin-left:6px;';
            btn.parentNode.appendChild(chatBtn);
        }
    })
    .catch(() => {
        btn.textContent = 'Error';
        btn.disabled = false;
    });
}
