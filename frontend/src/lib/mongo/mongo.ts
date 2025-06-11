// src/lib/mongo/mongo.ts

const mongoRoute = 'http://127.0.0.1:5000/api/mongo/updateUserPerson';
import { userID } from '../../authStore';

export async function updateUserInDB(newUserDetails:object, newPetDetails:object): Promise<{ success: boolean; message: string }> {
	try{
		let authID:any
		userID.subscribe(value => authID = value);

		const response = await fetch(mongoRoute, {
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