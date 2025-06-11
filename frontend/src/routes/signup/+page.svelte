<script>
  let email = "";
  let password = "";
  let confirmPassword = "";
  let phone = "";

  function handleSignup() {
    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }
    alert(`Signed up with ${email} and phone ${phone}`);
  }
</script>

<main class="signup-container">
  <h1>PetSpark</h1>
  <p class="subtitle">Create a PetSpark account</p>

  <form on:submit|preventDefault={handleSignup}>
    <input type="email" bind:value={email} placeholder="Email" required />
    <input
      type="password"
      bind:value={password}
      placeholder="Password"
      required
    />
    <input
      type="password"
      bind:value={confirmPassword}
      placeholder="Confirm password"
      required
    />
    <input type="tel" bind:value={phone} placeholder="Phone number" required />
    <button type="submit">Create Account</button>
  </form>

  <p class="login-link">
    Already have an account? <a href="/login">Log in</a>
  </p>

  <footer>&copy; 2025 UC Davis ECS 162</footer>
</main>

<style>
  .signup-container {
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

  .login-link {
    margin-top: 1rem;
  }

  .login-link a {
    color: #4285f4;
    text-decoration: none;
    margin-left: 0.25rem;
  }

  footer {
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #888;
  }
</style>
