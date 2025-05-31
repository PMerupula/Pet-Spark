// src/lib/authentication/auth.ts
import { createAuth0Client, Auth0Client } from '@auth0/auth0-spa-js'

let auth0: Auth0Client

export async function initAuth() 
{
    // Called when the page loads--sets up the Auth0 client and checks the user's authentication status
  auth0 = await createAuth0Client({
    domain: import.meta.env.VITE_AUTH0_DOMAIN,
    clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
    authorizationParams: {
      redirect_uri: window.location.origin, // where to redirect after login (goes back to the home page)
      audience: import.meta.env.VITE_AUTH0_AUDIENCE,
      scope: 'openid profile email'
    }
  })

  // Process redirect callback if user's coming back from Auth0 (i.e. they logged in either normally or after creating a user)
  if (window.location.search.includes('code=') && window.location.search.includes('state=')) {
    await auth0.handleRedirectCallback()
    window.history.replaceState({}, document.title, '/') // Clears the query parameters from the URL
  }

  // if the user is authenticated, print their user ID to the console
  const isAuthenticated = await auth0.isAuthenticated()
  if (isAuthenticated) 
{
    const user = await auth0.getUser()
    console.log('Logged in as:', user?.sub)
  }
}

// Redirects the user to the Auth0 login page 
export async function loginUser() {
  await auth0.loginWithRedirect()
}


// Logs the user out and redirects them to the home page
export async function logoutUser() {
  auth0.logout({
    logoutParams: {
      returnTo: window.location.origin
    }
  })
}