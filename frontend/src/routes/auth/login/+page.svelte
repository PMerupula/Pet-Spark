<script>
  import { goto } from '$app/navigation';
  import { loginUser } from '$lib/authentication/auth';

  let email = "";
  let password = "";
  let errorMessage = "";

  async function handleLogin() 
  {
    errorMessage = "";

    const result = await loginUser(email, password);
    if (!result.success) 
    {
      errorMessage = result.message;
    } 
    else 
    {
      goto('/dashboard');
    }
  }
</script>

<main class="login-container">
  <h1>PetSpark</h1>
  <p class="subtitle">Log in to your account</p>

  <form on:submit|preventDefault={handleLogin}>
    <input
      type="text"
      bind:value={email}
      placeholder="Email"
      required
    />
    <input
      type="password"
      bind:value={password}
      placeholder="Password"
      required
    />
    <button type="submit">Log In</button>
  </form>

  {#if errorMessage}
    <p class="error-message">{errorMessage}</p>
  {/if}

  <p class="signup-link">
    New to PetSpark?
    <a href="/auth/signup">Sign up</a>
  </p>

  <footer>&copy; 2025 UC Davis ECS 162</footer>
</main>

<style>
  .login-container {
    max-width: 400px;
    margin: 6rem auto;
    padding: 2rem;
    text-align: center;
    font-family: sans-serif;
    background-color: #f7f9fc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 0.25rem;
  }

  .subtitle {
    color: #555;
    margin-bottom: 2rem;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  input {
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 1rem;
  }

  button {
    background-color: #4285f4;
    color: white;
    padding: 0.75rem;
    font-size: 1rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }

  .signup-link {
    margin-top: 1rem;
  }

  .signup-link a {
    color: #4285f4;
    text-decoration: none;
    margin-left: 0.25rem;
  }

  footer {
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #888;
  }

  .success-message {
    margin-top: 1rem;
    padding: 0.75rem;
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    border-radius: 6px;
  }
</style>
