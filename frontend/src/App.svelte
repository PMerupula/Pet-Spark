<!-- src/App.svelte -->
<script lang="ts">
    import { isAuthenticated, createdNewUser, userAccessToken} from './authStore.ts';
    import { logoutUser } from './lib/authentication/auth.ts';
    import { onMount } from 'svelte';

    import RegisterForm from './lib/authentication/RegisterForm.svelte';
    import LoginForm from './lib/authentication/LoginForm.svelte';
    import UserPreferences from './lib/UserPreferences.svelte';
    import Dashboard from './lib/Dashboard.svelte';
    
    let currentView: 'landing' | 'login' | 'register' | 'preferences' | 'dashboard' = 'landing';

    $: if ($isAuthenticated) 
    {
    currentView = $createdNewUser ? 'preferences' : 'dashboard';
    }

    function logout() {
        logoutUser();
        currentView = 'landing';
    }

        function goToDashboard() {
        if ($isAuthenticated) {
            currentView = 'dashboard';
        } else {
            alert("You must be logged in to view the dashboard.");
            currentView = 'login';
        }
    }
</script>

<nav>
  <button on:click={() => currentView = 'landing'}>Landing Page</button>
  <button on:click={() => currentView = 'dashboard'}>Dashboard</button>
  {#if $isAuthenticated}
    <button on:click={logout}>Log out</button>
    {:else}
    <button on:click={() => currentView = 'login'}>Login</button>
    <button on:click={() => currentView = 'register'}>Register</button>
  {/if}
</nav>

<main>
  {#if currentView === 'landing'}
    <h1>Welcome to Pet Spark!</h1>
    <p>Find your ideal companion!</p>
  {:else if currentView === 'login'}
    <LoginForm switchToRegister={() => currentView = 'register'} />
  {:else if currentView === 'register'}
    <RegisterForm switchToLogin={() => currentView = 'login'} />
  {:else if currentView === 'preferences'}
    <UserPreferences />
  {:else if currentView === 'dashboard'}
    <Dashboard />
  {/if}
</main>