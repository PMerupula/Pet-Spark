<script lang="ts">
  import { initAuth, loginUser, logoutUser } from './lib/authentication/auth.ts'

  // Kick off the Auth0 setup when the component mounts
  initAuth()

  // Login/Register and logout call functions from auth.ts (will be changed to support custom UI)
  function handleLogin() 
  {
    loginUser()
  }

  function handleLogout() 
  {
    logoutUser()
  }
</script>

<main>
  <h1>Welcome to Pet Spark</h1>
  <button on:click={handleLogin}>Log In/Register</button>
  <button on:click={handleLogout}>Log Out</button>
</main>
