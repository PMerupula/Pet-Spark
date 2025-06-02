<script>
  let type = "";
  let breed = "";
  let age = "";
  let gender = "";
  let size = "";
  let location = "";

  const dogBreeds = [
    "Labrador Retriever", "German Shepherd Dog", "Golden Retriever", "Bulldog", "Beagle",
    "Poodle", "Rottweiler", "Yorkshire Terrier", "Boxer", "Dachshund",
    "Siberian Husky", "Great Dane", "Doberman Pinscher", "Australian Shepherd", "Shih Tzu",
    "Chihuahua", "Border Collie", "Cocker Spaniel", "Cavalier King Charles Spaniel", "Boston Terrier"
  ];

  const catBreeds = [
    "American Shorthair", "Siamese", "Maine Coon", "Persian", "Ragdoll",
    "Bengal", "British Shorthair", "Abyssinian", "Scottish Fold", "Sphynx",
    "Russian Blue", "Oriental Shorthair", "Norwegian Forest Cat", "Devon Rex", "Himalayan",
    "Manx", "Savannah", "Tonkinese", "Turkish Angora", "Bombay"
  ];

  const rabbitBreeds = [
    "Holland Lop", "Netherland Dwarf", "Mini Rex", "Lionhead", "Flemish Giant",
    "Mini Lop", "American", "English Lop", "French Lop"
  ];

  const breeds = {
    dog: dogBreeds,
    cat: catBreeds,
    rabbit: rabbitBreeds
  };

  function handleSubmit() {
    alert(`Preferences saved:
      Location: ${location}
      Type: ${type}
      Breed: ${breed}
      Age: ${age}
      Gender: ${gender}
      Size: ${size}`);
    // Later, send { location, type, breed, age, gender, size } to your backend/API
  }
</script>

<main class="filter-form">
  <h2>Set Your Pet Preferences</h2>

  <div class="field">
    <label>Location</label>
    <input
      type="text"
      bind:value={location}
      placeholder="Enter ZIP code or city"
    />
  </div>

  <div class="field">
    <label>Pet Type</label>
    <select bind:value={type}>
      <option value="">Any</option>
      <option value="dog">Dog</option>
      <option value="cat">Cat</option>
      <option value="rabbit">Critter</option>
    </select>
  </div>

  <div class="field">
    <label>Breed</label>
    <select bind:value={breed}>
      <option value="">Any</option>
      {#each breeds[type] as b}
        <option value={b}>{b}</option>
      {/each}
    </select>
  </div>

  <div class="field">
    <label>Age</label>
    <select bind:value={age}>
      <option value="">Any</option>
      <option value="baby">Kitten/Puppy</option>
      <option value="young">Young</option>
      <option value="adult">Adult</option>
      <option value="senior">Senior</option>
    </select>
  </div>

  <div class="field">
    <label>Gender</label>
    <select bind:value={gender}>
      <option value="">Any</option>
      <option value="male">Male</option>
      <option value="female">Female</option>
    </select>
  </div>

  <div class="field">
    <label>Size</label>
    <select bind:value={size}>
      <option value="">Any</option>
      <option value="small">Small</option>
      <option value="medium">Medium</option>
      <option value="large">Large</option>
      <option value="xlarge">X-Large</option>
    </select>
  </div>

  <button on:click={handleSubmit}>Save Preferences</button>
</main>

<style>
  .filter-form {
    max-width: 500px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #f8f9fa;
    border-radius: 12px;
    box-shadow: 0 0 8px rgba(0,0,0,0.05);
    font-family: sans-serif;
  }

  h2 {
    text-align: center;
    margin-bottom: 1.5rem;
  }

  .field {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    margin-bottom: 0.25rem;
    font-weight: bold;
  }

  input,
  select {
    width: 100%;
    padding: 0.5rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }

  button {
    margin-top: 1rem;
    width: 100%;
    padding: 0.75rem;
    font-size: 1rem;
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
</style>
