<!-- src/lib/authentication/RegisterForm.svelte -->

<script lang="ts">
    import { registerUser } from './auth';

    let email = '';
    let password = '';
    let errorMessage = '';
    let loading = false;

    async function handleRegister(event: Event)
    {
        event.preventDefault();
        loading = true;
        errorMessage = '';
        
        const result = await registerUser(email, password);
        loading = false;
        if(!result.success)
        {
            errorMessage = "Registration failed.";
        }
    }
</script>
<form on:submit={handleRegister}>
    <h2> Register </h2>
    <label for="email">Email:</label>
    <input type="email" id="email" bind:value={email} placeholder="Email" required />
    <label for="password">Password:</label>
    <input type="password" id="password" bind:value={password} placeholder="Password" required />
    <button type="submit" disabled={loading}>
        {#if loading}
            <p> Registering... </p>
        {:else}
            Register
        {/if}
    </button>
    {#if errorMessage}
        <p>{errorMessage}</p>
    {/if}

</form>