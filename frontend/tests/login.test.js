// @vitest-environment jsdom
import { test, expect } from 'vitest';
import { render } from '@testing-library/svelte';
import Login from '../src/routes/login/+page.svelte';

test('Login Page renders email/password inputs and button', () => {
  const { getByPlaceholderText, getByText } = render(Login);
  expect(getByPlaceholderText('Email/Phone number')).toBeInTheDocument();
  expect(getByPlaceholderText('Password')).toBeInTheDocument();
  expect(getByText('Log In')).toBeInTheDocument();
});
