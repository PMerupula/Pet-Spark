<script>
  import SwipeCard from '../components/SwipeCard.svelte';
  import PetGrid from '../components/PetGrid.svelte';

  let pets = [
    { id: 1, name: "Ginger", image: "/assets/u126.png" },
    { id: 2, name: "Coco", image: "/assets/1224212546.png" },
    { id: 3, name: "Buddy", image: "/assets/1222205652.png" },
    { id: 4, name: "Luna", image: "/assets/1229247178.png" },
    { id: 5, name: "Max", image: "/assets/1226328232.png" }
  ];

  let index = 0;
  function next() {
    index = (index + 1) % pets.length;
  }
  function prev() {
    index = (index - 1 + pets.length) % pets.length;
  }

  let type      = [];
  let gender    = "";
  let age       = "";
  let breed     = "";

  const dogBreeds    = [];
  const catBreeds    = [];
  const rabbitBreeds = [];
  const breeds = { dog: dogBreeds, cat: catBreeds, rabbit: rabbitBreeds };

  function applyFilter() {
    console.log({ type, gender, age, breed });
  }

</script>

<main>
  <!-- Hero -->
  <section class="hero">
    <h1>Ready to adopt a pet?</h1>
    <p>Let's get started. Search adoptable pets from shelters, rescues, and individuals.</p>
    <a href="/preferences" class="btn">Find Your Pet</a>
  </section>

  <!-- Carousel -->
  <section class="carousel">
    <button class="arrow prev" on:click={prev}>&lt;</button>
    <div class="card">
      <a href={`/petdetails/${pets[index].id}`}>
        <img src={pets[index].image} alt={pets[index].name} style="cursor:pointer;" />
      </a>
    </div>
    <button class="arrow next" on:click={next}>&gt;</button>
  </section>

  <div class="dots">
    {#each pets as _, i}
      <span class={i === index ? "dot active" : "dot"}></span>
    {/each}
  </div>

  <section class="filter-section">
    <div class="type-selection">
      <span class="looking-text">I’m looking for…</span>
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
          <option value="baby">Kitten/Puppy</option>
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

    <button class="apply-btn" on:click={applyFilter}>Apply</button>
  </section>

  <section class="recommended">
    <h2>Recommended Pets for You</h2>
    <PetGrid />
  </section>
</main>

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
  }
  .card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
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
  .type-selection label {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    cursor: pointer;
  }
  .filters-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .filter-item label {
    display: block;
    margin-bottom: 0.25rem;
    font-weight: bold;
  }
  .filter-item select {
    width: 100%;
    padding: 0.5rem;
    border-radius: 6px;
    border: 1px solid #ccc;
  }
  .apply-btn {
    display: block;
    margin: 0 auto;
    padding: 0.75rem 1.5rem;
    background: #4285f4;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
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
</style>
