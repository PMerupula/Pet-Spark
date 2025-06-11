<!-- src/lib/Dashboard.svelte -->

<script lang="ts">
    import { userID, isAuthenticated } from '../authStore.ts';
    import { logoutUser } from './authentication/auth.ts';

    function handleLogout()
    {
        logoutUser();
    }
</script>

{#if $isAuthenticated}
  <div>
    <h2>Dashboard</h2>
    <p>Welcome! Your Auth0 ID is: {$userID}</p>
  </div>
{:else}
  <p>You are not logged in.</p>
{/if}