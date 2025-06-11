// src/lib/mongo/mongo.ts

const mongoRouteUpdate = 'http://127.0.0.1:5000/api/mongo/updateUserPerson';
const mongoRouteGet = 'http://127.0.0.1:5000/api/mongo/getUserInfo';
import { userID } from '../../authStore';

export async function updateUserInDB(newUserDetails:object, newPetDetails:object): Promise<{ success: boolean; message: string }> {
	try{
		let authID:any
		userID.subscribe(value => authID = value);

		const response = await fetch(mongoRouteUpdate, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({authID, newUserDetails, newPetDetails})
		});
		const data = await response.json();
		console.log("mongo data: ", data);

		return { success: true, message: 'Mongo successful' };
	}
	catch (err) {
		console.error('Error mongoing:', err);
		return { success: false, message: 'Mongo error' };
	}
}

export async function getUserPreferences(): Promise<{ success: boolean; message: string; data: any }> {
	try{
		let authID:any
		userID.subscribe(value => authID = value);

		const response = await fetch(mongoRouteGet, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({authID})
		});
		const data = await response.json();
		console.log("mongo data: ", data);

		return { success: true, message: 'Mongo successful', data: data };
	}
	catch (err) {
		console.error('Error mongoing:', err);
		return { success: false, message: 'Mongo error', data: null };
	}
}

export async function verifyUserLoggedIn(): Promise<{ success: boolean; message: string }> {
	try{
		let authID:any
		userID.subscribe(value => authID = value);

		if(authID != null){
			return { success: true, message: 'User logged in' };
		}
		return { success: false, message: 'User not logged in' };
	}
	catch (err) {
		console.error('Error mongoing:', err);
		return { success: false, message: 'Mongo error' };
	}
}