// @vitest-environment jsdom
import { test, expect, vi } from 'vitest';
import { render, fireEvent } from '@testing-library/svelte';
import Preferences from '../src/routes/preferences/+page.svelte';

test('Preferences Page renders fields and submits correctly', async () => {
  const { getByLabelText, getByText } = render(Preferences);

  // Fill out the form
  await fireEvent.input(getByLabelText('Location'), { target: { value: '90210' } });
  await fireEvent.change(getByLabelText('Pet Type'), { target: { value: 'dog' } });
  await fireEvent.change(getByLabelText('Breed'), { target: { value: 'Beagle' } });

  // Spy on alert
  const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {});

  // Submit
  await fireEvent.click(getByText('Save Preferences'));

  expect(alertSpy).toHaveBeenCalledWith(expect.stringContaining('Location: 90210'));
  expect(alertSpy).toHaveBeenCalledWith(expect.stringContaining('Breed: Beagle'));
});
