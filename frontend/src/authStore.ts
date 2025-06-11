import {writable} from 'svelte/store';

export const isAuthenticated = writable(false);
export const userAccessToken = writable('');
export const createdNewUser = writable(false);
export const userID = writable<string | null>(null);