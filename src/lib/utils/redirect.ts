import { redirects } from './redirects';

export function redirectIfNeeded(pathname: string) {
    const normalized = pathname.toLowerCase().replace(/\/+$/, '');
    const target = redirects[normalized];
    
    if (target) {
        // Optional: show a temporary message
        const messageEl = document.createElement('div');
        messageEl.textContent = `Redirecting to ${target}…`;
        messageEl.style.position = 'fixed';
        messageEl.style.top = '50%';
        messageEl.style.left = '50%';
        messageEl.style.transform = 'translate(-50%, -50%)';
        messageEl.style.background = 'rgba(0,0,0,0.7)';
        messageEl.style.color = '#fff';
        messageEl.style.padding = '1rem 2rem';
        messageEl.style.borderRadius = '10px';
        messageEl.style.fontFamily = 'sans-serif';
        messageEl.style.fontSize = '1.2rem';
        document.body.appendChild(messageEl);

        // Slight delay so the user can see the message
        setTimeout(() => {
            window.location.href = target;
        }, 500); // 0.5s delay

        return true;
    }

    return false;
}
