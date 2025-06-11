<!-- src/lib/authentication/LoginForm.svelte -->

<script lang="ts">
    import { loginUser } from './auth';

    let email = '';
    let password = '';
    let errorMessage = '';
    let loading = false;

    async function handleLogin(event: Event)
    {
        event.preventDefault();
        loading = true;
        errorMessage = '';
        
        const result = await loginUser(email, password);
        //console.log('Login result:', result);
        loading = false;
        if(!result.success)
        {
            errorMessage = 'Login Failed.';
        }
    }
</script>
<form on:submit={handleLogin}>
    <h2> Login </h2>
    <label for="email">Email:</label>
    <input type="email" id="email" bind:value={email} placeholder="Email" required />
    <label for="password">Password:</label>
    <input type="password" id="password" bind:value={password} placeholder="Password" required />
    <button type="submit" disabled={loading}>
        {#if loading}
            <p> Logging in... </p>
        {:else}
            Log in
        {/if}
    </button>
    {#if errorMessage}
        <p>{errorMessage}</p>
    {/if}

</form>