// src/lib/authentication/auth.ts

import { userAccessToken, isAuthenticated } from "../../authStore";
import { createdNewUser } from "../../authStore";

const registerRoute = 'http://127.0.0.1:5000/api/authentication/register';
const loginRoute = 'http://127.0.0.1:5000/api/authentication/login';
const userIDRoute = 'https://dev-w53618ymk5dkjqz1.us.auth0.com/userinfo';
const getUserIDRoute = 'http://127.0.0.1/api/authentication/getuserid';
import { userID } from '../../authStore';

export async function registerUser(email: string, password: string): Promise<{ success: boolean; message: string }> {
	try {
		const response = await fetch(registerRoute, 
      {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ email, password })
		});


		const data = await response.json();
		if (!response.ok) 
    {
      userAccessToken.set('');
			return { success: false, message: data.error || 'Registration failed' };
		}
    isAuthenticated.set(true);
    createdNewUser.set(true);
    
    const accessToken = data.access_token;
    const thisUserID = data.user_id;

    userAccessToken.set(accessToken);
    userID.set(thisUserID);

		return { success: true, message: `Registered with user ID: ${data.user_id}` };
	} 
  catch (err) {
		console.error('Error registering user:', err);
		return { success: false, message: 'Network or server error' };
	}
}


export async function loginUser(email: string, password: string): Promise<{ success: boolean; token?: string; message: string }> {
	try {
		const response = await fetch(loginRoute, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ email, password })
		});

		const data = await response.json();

		if (!response.ok) {
			return { success: false, message: data.error || 'Login failed' };
		}
    isAuthenticated.set(true);
    
    const accessToken = data.access_token;
    const thisUserID = data.user_id;

    userAccessToken.set(accessToken);
    userID.set(thisUserID);

    console.log('Login successful, access token:', accessToken);
		return { success: true, token: accessToken, message: 'Login successful' };
	} catch (err) {
		console.error('Error logging in:', err);
		return { success: false, message: 'Network or server error' };
	}
}

export function logoutUser() 
{
  isAuthenticated.set(false);
  userAccessToken.set('');
  createdNewUser.set(false);
  userID.set(null);
}

export async function getUserID(token: string): Promise<{ success: boolean; userId?: string}> 
{
  try {
    const response = await fetch(getUserIDRoute, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!response.ok) {
      const error = await response.json();
      console.error("Failed to get user ID:", error);
      return { success: false };
    }

    const data = await response.json();
    return { success: true, userId: data.user_id };
  } catch (err) {
    console.error("Error calling /getuserid:", err);
    return { success: false };
  }
}