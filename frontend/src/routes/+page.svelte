<script>
  import { onMount } from 'svelte';
  import PetCard from '../components/PetCard.svelte'; 


  let defaultPets = [
    { id: 1, name: "Ginger", image: "/assets/u126.png" },
    { id: 2, name: "Coco", image: "/assets/1224212546.png" },
    { id: 3, name: "Buddy", image: "/assets/1222205652.png" },
    { id: 4, name: "Luna", image: "/assets/1229247178.png" },
    { id: 5, name: "Max", image: "/assets/1226328232.png" }
  ];

  let pets = [];
  let recommendedPets = [];
  let loading = false;
  let error = null;
  let recommendedLoading = true;

  let showModal = false;
  let selectedPet = null;

  let index = 0;
  function next() {
    index = (index + 1) % pets.length;
  }
  function prev() {
    index = (index - 1 + pets.length) % pets.length;
  }

  let type = [];
  let gender = "";
  let age = "";
  let breed = "";
  let location = "Davis, CA"; // Davis for default, to show how it's formatted

  const dogBreeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Poodle"];
  const catBreeds = ["Domestic Short Hair", "Domestic Long Hair", "Siamese", "Persian", "Maine Coon"];
  const rabbitBreeds = ["Holland Lop", "Netherland Dwarf", "Lionhead", "Mini Rex", "Flemish Giant"];
  const breeds = { dog: dogBreeds, cat: catBreeds, rabbit: rabbitBreeds };

  async function showPetDetails(pet) {
    if (!pet.realPet) return;
    
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/pets/${pet.petId}`);
      const data = await response.json();
      
      console.log('Pet details:', data);
      
      if (data.animal) {
        selectedPet = {
          name: data.animal.name,
          photos: data.animal.photos || [],
          age: data.animal.age,
          gender: data.animal.gender,
          size: data.animal.size,
          breed: data.animal.breeds?.primary || 'Mixed',
          color: data.animal.colors?.primary || 'Unknown',
          description: data.animal.description || 'No description available',
          location: `${data.animal.contact.address.city}, ${data.animal.contact.address.state}`,
          email: data.animal.contact.email,
          phone: data.animal.contact.phone,
          attributes: data.animal.attributes || {},
          environment: data.animal.environment || {},
          tags: data.animal.tags || []
        };
        showModal = true;
      }
    } catch (err) {
      console.error('Error fetching pet details:', err);
      error = 'Failed to load pet details';
    }
  }

  async function fetchPetsForCarousel() {
    try {
      const res = await fetch(`http://127.0.0.1:5000/api/pets?location=${encodeURIComponent(location)}&sort=random&limit=5`);
      const data = await res.json();
      if (data.animals && data.animals.length > 0) {
        pets = data.animals.map(animal => ({
          id: animal.id,
          name: animal.name,
          image: animal.photos?.[0]?.large || animal.photos?.[0]?.medium || animal.photos?.[0]?.small || '/assets/placeholder.png',
          realPet: true,
          location: `${animal.contact.address.city}, ${animal.contact.address.state}`,
          age: animal.age,
          gender: animal.gender,
          petId: animal.id
        }));
        index = 0;
      } else {
        pets = [...defaultPets];
        index = 0;
      }
    } catch (err) {
      pets = [...defaultPets];
      index = 0;
    }
  }


  function closeModal() {
    showModal = false;
    selectedPet = null;
  }

  async function applyFilter() {
    console.log('Applying filters:', { type, gender, age, breed, location });
    
    if (type.length === 0 && !gender && !age && !breed) {
      pets = [...defaultPets];
      index = 0;
      return;
    }

    loading = true;
    error = null;
    
    try {
      const params = new URLSearchParams();
      
      if (type.length > 0) {
        type.forEach(t => {
          params.append('type', t);
        });
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
      
      params.append('limit', '10');
      params.append('sort', 'random');
      
      const response = await fetch(`http://127.0.0.1:5000/api/pets?${params.toString()}`);
      const data = await response.json();
      
<<<<<<< HEAD
      const processedPets = data.animals?.map((animal, i) => ({
=======
      console.log('Filtered pets API Response:', data);
      
      let filteredPets = data.animals?.map((animal, i) => ({
>>>>>>> c998153d431a6ecae20d0de257c7a0fbd8bbcf11
        id: `filtered_${i}`,
        name: animal.name,
        image: animal.photos?.[0]?.large || animal.photos?.[0]?.medium || animal.photos?.[0]?.small || '/assets/placeholder.png',
        realPet: true,
        location: `${animal.contact.address.city}, ${animal.contact.address.state}`,
        age: animal.age,
        gender: animal.gender,
        petId: animal.id
      })) || [];
      
      if (processedPets.length > 0) {
        pets = processedPets;
        index = 0; 
        console.log('Updated carousel with filtered pets:', pets);
      } else {
        error = "No pets found matching your criteria. Try different filters!";
        pets = [...defaultPets]; 
      }
      
    } catch (err) {
      error = err.message;
      console.error('Error fetching filtered pets:', err);
      pets = [...defaultPets]; 
    } finally {
      loading = false;
    }
  }

  function resetFilters() {
    type = [];
    gender = "";
    age = "";
    breed = "";
    location = "Davis, CA";
    pets = [...defaultPets];
    index = 0;
    error = null;
  }

  async function fetchRandomPetsForRecommendation() {
    try {
      recommendedLoading = true;
      // Get 20 random pets
      const response = await fetch(`http://127.0.0.1:5000/api/pets?sort=random&limit=20`);
      const data = await response.json();
      
      console.log('Random pets for recommendation:', data);
      
      if (data.animals && data.animals.length > 0) {
        recommendedPets = data.animals.map(animal => ({
          name: animal.name,
          location: `${animal.contact.address.city}, ${animal.contact.address.state}`,
          age: animal.age,
          gender: animal.gender,
          color: animal.colors?.primary || 'Unknown',
          houseTrained: animal.attributes?.house_trained ? 'Yes' : 'No',
          health: animal.attributes?.spayed_neutered ? 'Spayed/Neutered' : 'Not specified',
          about: animal.description || 'No description available',
          imageUrl: animal.photos?.[0]?.large || animal.photos?.[0]?.medium || animal.photos?.[0]?.small || ''
        }));
      } else {
        recommendedPets = [];
      }
      
    } catch (err) {
      console.error('Error fetching random pets:', err);
      recommendedPets = [];
    } finally {
      recommendedLoading = false;
    }
  }

  onMount(() => {
    fetchRandomPetsForRecommendation(); 
    fetchPetsForCarousel();
  });
</script>

<main>
  <!-- Hero -->
  <section class="hero">
    <h1>Ready to adopt a pet?</h1>
    <p>Let's get started. Search adoptable pets from shelters, rescues, and individuals.</p>
    <a href="/pets" class="btn">Find Your Pet</a>
  </section>

  <!-- Carousel -->
  <section class="carousel">
    {#if pets.length === 0}
      <div class="card" style="display:flex;align-items:center;justify-content:center;color:#888;font-size:1.5rem;">
        Loading pets...
      </div>
    {:else}
      <button class="arrow prev" on:click={prev}>&lt;</button>
      <div class="card">
        {#if pets[index]?.realPet}
          <div class="real-pet-info" on:click={() => showPetDetails(pets[index])} style="cursor: pointer;">
            <img src={pets[index].image} alt={pets[index].name} />
            <div class="pet-overlay">
              <h3>{pets[index].name}</h3>
              <p>{pets[index].location}</p>
              <p>{pets[index].age} • {pets[index].gender}</p>
              <p class="click-hint">Click for details</p>
            </div>
          </div>
        {:else}
          <a href={`/petdetails/${pets[index]?.id}`}>
            <img src={pets[index]?.image} alt={pets[index]?.name} style="cursor:pointer;" />
          </a>
        {/if}
      </div>
      <button class="arrow next" on:click={next}>&gt;</button>
    {/if}
  </section>


  <div class="dots">
    {#each pets as _, i}
      <span class={i === index ? "dot active" : "dot"}></span>
    {/each}
  </div>

  <!-- Filter Section -->
  <section class="filter-section">
    <div class="type-selection">
      <span class="looking-text">I'm looking for…</span>
      <label>
        <input type="checkbox" bind:group={type} value="dog" />
        <img src="/assets/Dogs.png" alt="Dogs" class="type-icon" />
        <span>Dogs</span>
      </label>

      <label>
        <input type="checkbox" bind:group={type} value="cat" />
        <img src="/assets/Cats.png" alt="Cats" class="type-icon" />
        <span>Cats</span>
      </label>

      <label>
        <input type="checkbox" bind:group={type} value="rabbit" />
        <img src="/assets/Critters.png" alt="Critters" class="type-icon" />
        <span>Critters</span>
      </label>
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
        <label>Looks Like</label>
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
    </div>

    <div class="filter-actions">
      <button class="apply-btn" on:click={applyFilter} disabled={loading}>
        {loading ? 'Loading...' : 'Apply'}
      </button>
      <button class="reset-btn" on:click={resetFilters}>Reset</button>
    </div>

    {#if error}
      <p class="error-message">{error}</p>
    {/if}
  </section>

  <section class="recommended">
    <h2>Give These Pets a Chance! 🐾</h2>
    <p class="section-subtitle">These amazing pets are looking for their forever homes</p>
    
    {#if recommendedLoading}
      <p style="text-align: center; color: #666;">🐾 Loading pets...</p>
    {:else if recommendedPets.length > 0}
      <div class="pets-container">
        {#each recommendedPets as pet}
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
      <p style="text-align: center; color: #666;">No pets available right now. Check back soon!</p>
    {/if}
  </section>
</main>

{#if showModal && selectedPet}
  <div class="modal-overlay" on:click={closeModal}>
    <div class="modal-content" on:click|stopPropagation>
      <button class="close-btn" on:click={closeModal}>&times;</button>
      
      <div class="modal-header">
        <h2>{selectedPet.name}</h2>
        <p class="location">{selectedPet.location}</p>
      </div>

      <div class="modal-body">
        <div class="pet-photos">
          {#if selectedPet.photos.length > 0}
            <img src={selectedPet.photos[0].large || selectedPet.photos[0].medium || selectedPet.photos[0].small} alt={selectedPet.name} />
          {:else}
            <div class="no-photo">No photo available</div>
          {/if}
        </div>

        <div class="pet-info">
          <div class="info-grid">
            <div class="info-item">
              <strong>Age:</strong> {selectedPet.age}
            </div>
            <div class="info-item">
              <strong>Gender:</strong> {selectedPet.gender}
            </div>
            <div class="info-item">
              <strong>Size:</strong> {selectedPet.size}
            </div>
            <div class="info-item">
              <strong>Breed:</strong> {selectedPet.breed}
            </div>
            <div class="info-item">
              <strong>Color:</strong> {selectedPet.color}
            </div>
          </div>

          {#if selectedPet.description}
            <div class="description">
              <h3>About {selectedPet.name}</h3>
              <p>{selectedPet.description}</p>
            </div>
          {/if}

          <div class="attributes">
            <h3>Pet Characteristics</h3>
            <div class="attributes-grid">
              <div class="attribute">
                <strong>House Trained:</strong> {selectedPet.attributes.house_trained ? 'Yes' : 'No'}
              </div>
              <div class="attribute">
                <strong>Spayed/Neutered:</strong> {selectedPet.attributes.spayed_neutered ? 'Yes' : 'No'}
              </div>
              <div class="attribute">
                <strong>Good with Kids:</strong> {selectedPet.environment.children !== null ? (selectedPet.environment.children ? 'Yes' : 'No') : 'Unknown'}
              </div>
              <div class="attribute">
                <strong>Good with Dogs:</strong> {selectedPet.environment.dogs !== null ? (selectedPet.environment.dogs ? 'Yes' : 'No') : 'Unknown'}
              </div>
              <div class="attribute">
                <strong>Good with Cats:</strong> {selectedPet.environment.cats !== null ? (selectedPet.environment.cats ? 'Yes' : 'No') : 'Unknown'}
              </div>
            </div>
          </div>

          {#if selectedPet.tags.length > 0}
            <div class="tags">
              <h3>Personality</h3>
              <div class="tag-list">
                {#each selectedPet.tags as tag}
                  <span class="tag">{tag}</span>
                {/each}
              </div>
            </div>
          {/if}

          <div class="contact-info">
            <h3>Contact Information</h3>
            {#if selectedPet.email}
              <p><strong>Email:</strong> {selectedPet.email}</p>
            {/if}
            {#if selectedPet.phone}
              <p><strong>Phone:</strong> {selectedPet.phone}</p>
            {/if}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  :global(body) {
    margin: 0;
    font-family: sans-serif;
    background: #f4f6f8;
  }
  
  .hero {
    width: 100%;
    background: #eaf4fe;
    text-align: center;
    padding: 2.5rem 1rem;
  }
  .hero h1 {
    font-size: 2.5rem;
    margin: 0 0 1rem;
    color: #333;
  }
  .hero p {
    font-size: 1.25rem;
    margin: 0 0 1.5rem;
    color: #555;
  }
  .btn {
    background: #4285f4;
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    font-size: 1.1rem;
    text-decoration: none;
  }
  .btn:hover {
    background: #336ac4;
  }

  .carousel {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2rem 0;
    padding: 0 2rem;
  }
  .card {
    width: 900px;   
    height: 700px; 
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    overflow: hidden;
    position: relative;
  }
  .card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .real-pet-info {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.2s;
  }

  .real-pet-info:hover {
    transform: scale(1.02);
  }

  .pet-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.8));
    color: white;
    padding: 2rem;
    text-align: left;
  }

  .pet-overlay h3 {
    font-size: 2rem;
    margin: 0 0 0.5rem;
  }

  .pet-overlay p {
    margin: 0.25rem 0;
    font-size: 1.1rem;
  }

  .click-hint {
    font-size: 0.9rem;
    opacity: 0.8;
    font-style: italic;
    margin-top: 0.5rem !important;
  }

  .arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    font-size: 3rem;
    color: rgba(0, 0, 0, 0.6);
    cursor: pointer;
    z-index: 5;
  }
  .arrow:hover {
    color: rgba(0, 0, 0, 0.9);
  }
  .prev {
    left: calc((100% - 900px) / 2 - 4rem);
  }
  .next {
    right: calc((100% - 900px) / 2 - 4rem);
  }

  .dots {
    text-align: center;
    margin-bottom: 2rem;
  }
  .dot {
    display: inline-block;
    width: 16px;
    height: 16px;
    margin: 0 6px;
    border-radius: 50%;
    background: #ccc;
  }
  .dot.active {
    background: #666;
  }

  .filter-section {
    max-width: 960px;
    margin: 2rem auto;
    padding: 1rem;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  .type-selection {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }
 
  .filters-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .filter-item label {
    display: block;
    margin-bottom: 0.25rem;
    font-weight: bold;
  }
  .filter-item select,
  .filter-item input {
    width: 100%;
    padding: 0.5rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }

  .filter-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }

  .apply-btn {
    padding: 0.75rem 1.5rem;
    background: #4285f4;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
  }

  .apply-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
  }

  .reset-btn {
    padding: 0.75rem 1.5rem;
    background: #f8f9fa;
    color: #666;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
  }

  .reset-btn:hover {
    background: #e9ecef;
  }

  .error-message {
    text-align: center;
    color: #e74c3c;
    margin-top: 1rem;
    padding: 0.75rem;
    background: #fdf2f2;
    border-radius: 6px;
  }

  .recommended {
    max-width: 960px;
    margin: 3rem auto;
    padding: 0 1rem;
  }
  .recommended h2 {
    text-align: center;
    font-size: 1.75rem;
    color: #333;
    margin-bottom: 1rem;
  }

  .type-selection label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .type-icon {
    width: 50px;
    height: 50px;
    object-fit: contain;
  }

  /* Modal Styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    padding: 1rem;
  }

  .modal-content {
    background: white;
    border-radius: 12px;
    max-width: 800px;
    max-height: 90vh;
    width: 100%;
    overflow-y: auto;
    position: relative;
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: #666;
    z-index: 1001;
  }

  .close-btn:hover {
    color: #000;
  }

  .modal-header {
    padding: 2rem 2rem 1rem;
    border-bottom: 1px solid #eee;
  }

  .modal-header h2 {
    margin: 0 0 0.5rem;
    font-size: 2rem;
    color: #333;
  }

  .location {
    margin: 0;
    color: #666;
    font-size: 1.1rem;
  }

  .modal-body {
    padding: 2rem;
  }

  .pet-photos img {
    width: 100%;
    max-height: 400px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 2rem;
  }

  .no-photo {
    background: #f8f9fa;
    padding: 3rem;
    text-align: center;
    border-radius: 8px;
    color: #666;
    margin-bottom: 2rem;
  }

  .info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }

  .info-item {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 6px;
  }

  .description {
    margin-bottom: 2rem;
  }

  .description h3 {
    color: #333;
    margin-bottom: 1rem;
  }

  .description p {
    line-height: 1.6;
    color: #555;
  }

  .attributes {
    margin-bottom: 2rem;
  }

  .attributes h3 {
    color: #333;
    margin-bottom: 1rem;
  }

  .attributes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.5rem;
  }

  .attribute {
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
  }

  .tags {
    margin-bottom: 2rem;
  }

  .tags h3 {
    color: #333;
    margin-bottom: 1rem;
  }

  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .tag {
    background: #e3f2fd;
    color: #1976d2;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.9rem;
  }

  .contact-info h3 {
    color: #333;
    margin-bottom: 1rem;
  }

  .contact-info p {
    margin: 0.5rem 0;
  }

  @media (max-width: 768px) {
    .filters-grid {
      grid-template-columns: 1fr;
    }
    
    .modal-content {
      margin: 1rem;
      max-height: 95vh;
    }
    
    .modal-body {
      padding: 1rem;
    }
    
    .info-grid {
      grid-template-columns: 1fr;
    }
  }

  .pets-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .looking-text {
    font-weight: bold;
    color: #333;
    margin-right: 1rem;
  }

  .section-subtitle {
    text-align: center;
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 2rem;
    font-style: italic;
  }
</style>
