<script>
    import { isAuthenticated } from '../authStore';
    import { logoutUser } from '$lib/authentication/auth'; // your logout function
    import { goto } from '$app/navigation';
    import { get } from 'svelte/store';

    function handleLogout()
    {
        logoutUser();
        isAuthenticated.set(false);
        goto('/');
    }
</script>

<div class="navbar">
    <div class="nav-left">
        <a href="/" class="logo-link">PetSpark</a>
    </div>

    <div class="nav-right">
        {#if $isAuthenticated}
            <a href="/preferences" class="preferences-icon" aria-label="Preferences">♥️</a>
            <a href="#" on:click|preventDefault={handleLogout}>Log out</a>
        {:else}
        <a href="/auth/login">Log in</a>
        <a href="/auth/signup">Sign up</a>
        
        {/if}
        <!-- <span>{username}</span> -->

    </div>
</div>
<div class="spacer"></div>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
    }

    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        background-color: #4285f4;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-sizing: border-box;
        z-index: 1000;
    }

    .spacer {
        height: 4.5rem;
    }

    .nav-left,
    .nav-right {
        display: flex;
        align-items: center;
    }

    .nav-left {
        gap: 0.5rem;
    }

    .nav-right {
        gap: 1rem;
    }

    .nav-left a,
    .nav-right a {
        text-decoration: none !important;
        color: white !important;
    }

    .icon {
        font-size: 1.3rem;
        cursor: pointer;
    }

    .logo-link {
        font-size: 1.3rem;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .preferences-icon {
        font-size: 1.3rem;
    }

</style>

