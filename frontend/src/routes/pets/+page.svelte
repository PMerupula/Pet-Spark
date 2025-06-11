<script>
  import { onMount } from 'svelte';
  import PetCard from '../../components/PetCard.svelte';
  
  let pets = [];
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/pets?location=95816&sort=random');
      const data = await response.json();
      
      // ADD THESE DEBUG LINES:
      console.log('API Response:', data);
      console.log('Number of animals:', data.animals?.length);
      
      pets = data.animals?.map(animal => ({
        name: animal.name,
        location: `${animal.contact.address.city}, ${animal.contact.address.state}`,
        age: animal.age,
        gender: animal.gender,
        color: animal.colors?.primary || 'Unknown',
        houseTrained: animal.attributes?.house_trained ? 'Yes' : 'No',
        health: animal.attributes?.spayed_neutered ? 'Spayed/Neutered' : 'Not specified',
        about: animal.description || 'No description available',
        imageUrl: animal.photos?.[0]?.large || animal.photos?.[0]?.medium || animal.photos?.[0]?.small || ''
      })) || [];
      
      // ADD THIS DEBUG LINE:
      console.log('Processed pets:', pets);
      
    } catch (err) {
      error = err.message;
      console.error('Error fetching pets:', err);
    } finally {
      loading = false;
    }
  });
</script>

<main>
  <h1>Available Pets</h1>
  
  {#if loading}
    <p>Loading pets...</p>
  {:else if error}
    <p>Error: {error}</p>
  {:else if pets.length > 0}
    {#each pets as pet}
      <PetCard 
        name={pet.name}
        location={pet.location}
        age={pet.age}
        gender={pet.gender}
        color={pet.color}
        houseTrained={pet.houseTrained}
        health={pet.health}
        about={pet.about}
        imageUrl={pet.imageUrl}
      />
    {/each}
  {:else}
    <p>No pets found.</p>
  {/if}
</main>