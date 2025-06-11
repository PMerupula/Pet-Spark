<script>
  import { onMount } from 'svelte';
  import PetCard from '../../components/PetCard.svelte';
  
  let pets = [];
  let loading = true;
  let error = null;

  let type = [];
  let gender = "";
  let age = "";
  let breed = "";
  let location = "Davis, CA"; 
  let limit = 50; 

  const dogBreeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Poodle"];
  const catBreeds = ["Domestic Short Hair", "Domestic Long Hair", "Siamese", "Persian", "Maine Coon"];
  const rabbitBreeds = ["Holland Lop", "Netherland Dwarf", "Lionhead", "Mini Rex", "Flemish Giant"];
  const breeds = { dog: dogBreeds, cat: catBreeds, rabbit: rabbitBreeds };

  async function fetchPets() {
    loading = true;
    error = null;
    
    try {
      const params = new URLSearchParams();
      
      if (type.length > 0) {
        params.append('type', type.join(','));
      }
      if (gender) {
        params.append('gender', gender);
      }
      if (age) {
        params.append('age', age);
      }
      if (breed) {
        params.append('breed', breed);
      }
      if (location) {
        params.append('location', location);
      }
      
      // Add limit parameter
      params.append('limit', limit);
      params.append('sort', 'random');
      
      const response = await fetch(`http://127.0.0.1:5000/api/pets?${params.toString()}`);
      const data = await response.json();
      
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
      
      console.log('Processed pets:', pets);
      
    } catch (err) {
      error = err.message;
      console.error('Error fetching pets:', err);
    } finally {
      loading = false;
    }
  }

  function applyFilter() {
    console.log('Applying filters:', { type, gender, age, breed, location, limit });
    fetchPets();
  }

  function resetFilters() {
    type = [];
    gender = "";
    age = "";
    breed = "";
    location = "Davis, CA"; 
    limit = 50;
    fetchPets();
  }

  onMount(() => {
    fetchPets();
  });
</script>

<main>
  <div class="header">
    <h1>Available Pets</h1>
    <p>Find your perfect companion with our advanced filters</p>
  </div>

  <section class="filter-section">
    <div class="filter-header">
      <h2>Filter Pets</h2>
      <button class="reset-btn" on:click={resetFilters}>Reset All</button>
    </div>

    <div class="filters-container">
      <div class="type-selection">
        <span class="filter-label">I'm looking for…</span>
        <div class="type-options">
          <label class="type-option">
            <input type="checkbox" bind:group={type} value="dog" />
            <img src="/assets/Dogs.png" alt="Dogs" class="type-icon" />
            <span>Dogs</span>
          </label>

          <label class="type-option">
            <input type="checkbox" bind:group={type} value="cat" />
            <img src="/assets/Cats.png" alt="Cats" class="type-icon" />
            <span>Cats</span>
          </label>

          <label class="type-option">
            <input type="checkbox" bind:group={type} value="rabbit" />
            <img src="/assets/Critters.png" alt="Critters" class="type-icon" />
            <span>Critters</span>
          </label>
        </div>
      </div>

      <div class="filters-grid">
        <div class="filter-item">
          <label>Location (City, State)</label>
          <input 
            type="text" 
            bind:value={location} 
            placeholder="e.g., Davis, CA or San Francisco, CA"
          />
        </div>

        <div class="filter-item">
          <label>Gender</label>
          <select bind:value={gender}>
            <option value="">All genders</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>

        <div class="filter-item">
          <label>Age</label>
          <select bind:value={age}>
            <option value="">All ages</option>
            <option value="baby">Baby</option>
            <option value="young">Young</option>
            <option value="adult">Adult</option>
            <option value="senior">Senior</option>
          </select>
        </div>

        <div class="filter-item">
          <label>Breed</label>
          <select bind:value={breed}>
            <option value="">All breeds</option>
            {#if type.includes('dog')}
              {#each breeds.dog as b}<option value={b}>{b}</option>{/each}
            {/if}
            {#if type.includes('cat')}
              {#each breeds.cat as b}<option value={b}>{b}</option>{/each}
            {/if}
            {#if type.includes('rabbit')}
              {#each breeds.rabbit as b}<option value={b}>{b}</option>{/each}
            {/if}
          </select>
        </div>

        <div class="filter-item">
          <label>Number of Results</label>
          <select bind:value={limit}>
            <option value={20}>20 pets</option>
            <option value={50}>50 pets</option>
            <option value={100}>100 pets</option>
          </select>
        </div>
      </div>

      <button class="apply-btn" on:click={applyFilter}>
        Apply Filters ({pets.length} pets found)
      </button>
    </div>
  </section>

  <section class="results-section">
    {#if loading}
      <div class="loading">
        <p>🐾 Loading pets...</p>
      </div>
    {:else if error}
      <div class="error">
        <p>Error: {error}</p>
        <button on:click={fetchPets}>Try Again</button>
      </div>
    {:else if pets.length > 0}
      <div class="pets-container">
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
      </div>
    {:else}
      <div class="no-results">
        <p>🔍 No pets found with your current filters.</p>
        <p>Try adjusting your search criteria or <button class="link-btn" on:click={resetFilters}>reset all filters</button>.</p>
      </div>
    {/if}
  </section>
</main>

<style>
  :global(body) {
    margin: 0;
    font-family: sans-serif;
    background: #f4f6f8;
  }

  main {
    min-height: 100vh;
    padding-bottom: 2rem;
  }

  .header {
    background: #eaf4fe;
    text-align: center;
    padding: 2rem 1rem;
  }

  .header h1 {
    font-size: 2.5rem;
    margin: 0 0 0.5rem;
    color: #333;
  }

  .header p {
    font-size: 1.1rem;
    color: #666;
    margin: 0;
  }

  .filter-section {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
  }

  .filter-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
  }

  .filter-header h2 {
    color: #333;
    margin: 0;
  }

  .reset-btn {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    color: #666;
  }

  .reset-btn:hover {
    background: #e9ecef;
  }

  .filters-container {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.1);
  }

  .type-selection {
    margin-bottom: 2rem;
  }

  .filter-label {
    display: block;
    font-weight: bold;
    margin-bottom: 1rem;
    color: #333;
  }

  .type-options {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
  }

  .type-option {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
    padding: 1rem;
    border-radius: 8px;
    transition: background-color 0.2s;
  }

  .type-option:hover {
    background: #f8f9fa;
  }

  .type-icon {
    width: 50px;
    height: 50px;
    object-fit: contain;
  }

  .filters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .filter-item label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #333;
  }

  .filter-item input,
  .filter-item select {
    width: 100%;
    padding: 0.75rem;
    border-radius: 6px;
    border: 1px solid #ddd;
    font-size: 1rem;
    box-sizing: border-box;
  }

  .filter-item input:focus,
  .filter-item select:focus {
    outline: none;
    border-color: #4285f4;
    box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.2);
  }

  .apply-btn {
    display: block;
    margin: 0 auto;
    padding: 1rem 2rem;
    background: #4285f4;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: bold;
    transition: background-color 0.2s;
  }

  .apply-btn:hover {
    background: #3367d6;
  }

  .results-section {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
  }

  .loading, .error, .no-results {
    text-align: center;
    padding: 3rem 1rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.1);
  }

  .loading p {
    font-size: 1.2rem;
    color: #666;
  }

  .error p {
    color: #e74c3c;
    margin-bottom: 1rem;
  }

  .error button {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    cursor: pointer;
  }

  .no-results p {
    color: #666;
    margin: 0.5rem 0;
  }

  .link-btn {
    background: none;
    border: none;
    color: #4285f4;
    cursor: pointer;
    text-decoration: underline;
    font-size: inherit;
  }

  .pets-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  @media (max-width: 768px) {
    .header h1 {
      font-size: 2rem;
    }

    .type-options {
      justify-content: center;
    }

    .filters-grid {
      grid-template-columns: 1fr;
    }

    .filter-header {
      flex-direction: column;
      gap: 1rem;
      text-align: center;
    }
  }
</style>