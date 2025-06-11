// @vitest-environment jsdom
import { test, expect } from 'vitest';
import { render } from '@testing-library/svelte';
import Signup from '../src/routes/signup/+page.svelte';

test('Signup Page renders signup form fields and button', () => {
  const { getByPlaceholderText, getByText } = render(Signup);
  expect(getByPlaceholderText('Email')).toBeInTheDocument();
  expect(getByPlaceholderText('Password')).toBeInTheDocument();
  expect(getByPlaceholderText('Confirm password')).toBeInTheDocument();
  expect(getByPlaceholderText('Phone number')).toBeInTheDocument();
  expect(getByText('Create Account')).toBeInTheDocument();
});
