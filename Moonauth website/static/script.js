document.addEventListener('DOMContentLoaded', () => {
    const authBtn = document.getElementById('auth-btn');

    // Generate Discord OAuth URL
    authBtn.addEventListener('click', (e) => {
        e.preventDefault();

        const clientId = 'YOUR_CLIENT_ID'; // REPLACE WITH YOUR CLIENT ID
        const redirectUri = encodeURIComponent(window.location.origin + '/auth/callback');
        const scope = encodeURIComponent('identify guilds.join');

        const authUrl = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&scope=${scope}`;

        window.location.href = authUrl;
    });

    // Check for successful verification
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('verified')) {
        console.log('User successfully verified!');
        // Add any post-verification logic here
    }
});