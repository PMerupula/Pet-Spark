// @vitest-environment jsdom
import { test, expect } from 'vitest';
import { render } from '@testing-library/svelte';
import Home from '../src/routes/+page.svelte';

test('Home Page renders hero heading and button', () => {
  const { getByText } = render(Home);
  expect(getByText('Ready to adopt a pet?')).toBeInTheDocument();
  expect(getByText('Find Your Pet')).toBeInTheDocument();
});
