<script>
  let pets = [
    { name: "Ginger", image: "/u126.png" },
    { name: "Coco", image: "/1224212546.png" },
    { name: "Buddy", image: "/1222205652.png" },
    { name: "Luna", image: "/1229247178.png" },
    { name: "Max", image: "/1226328232.png" }
  ];

  let index = 0;

  function next() {
    index = (index + 1) % pets.length;
  }

  function prev() {
    index = (index - 1 + pets.length) % pets.length;
  }
</script>

<nav class="navbar">
  <div class="logo">PetSpark</div>
  <div class="nav-links">
    <a href="/login">Log in</a>
    <a href="/signup">Sign up</a>
  </div>
</nav>

<main>
  <!-- Hero Section -->
  <section class="hero">
    <h1>Ready to adopt a pet?</h1>
    <p>
      Let's get started. Search adoptable pets from shelters, rescues, and individuals.
    </p>
    <a href="/preferences" class="btn">Find Your Pet</a>
  </section>

  <!-- Carousel Section -->
  <section class="carousel">
    <button class="arrow" on:click={prev}>&lt;</button>
    <div class="card">
      <img src={pets[index].image} alt={pets[index].name} />
    </div>
    <button class="arrow" on:click={next}>&gt;</button>
  </section>

  <div class="dots">
    {#each pets as _, i}
      <span class={i === index ? 'dot active' : 'dot'}></span>
    {/each}
  </div>
</main>

<style>
  /* Navbar */
  .navbar {
    display: flex;
    justify-content: space-between;
    padding: 1rem 2rem;
    background-color: #4285f4;
    color: white;
    font-size: 1.2rem;
  }
  .nav-links a {
    margin-left: 1rem;
    color: white;
    text-decoration: none;
  }

  /* Main Layout */
  main {
    max-width: 900px;
    margin: 2rem auto;
    padding: 0 1rem;
    font-family: sans-serif;
  }

  /* Hero Section (smaller) */
  .hero {
    text-align: center;
    background-color: #f0f8ff;
    padding: 1rem 0.5rem;
    border-radius: 5px;
    margin-bottom: 0.5rem;
  }
  .hero h1 {
    font-size: 1.5rem;
    margin-bottom: 0.25rem;
    color: #333;
  }
  .hero p {
    font-size: 1rem;
    color: #555;
    margin-bottom: 1rem;
  }
  .btn {
    display: inline-block;
    background-color: #4285f4;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    font-size: 0.9rem;
  }
  .btn:hover {
    background-color: #336ac4;
  }

  /* Carousel Section */
  .carousel {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .card {
    max-width: 500px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    overflow: hidden;
  }
  .card img {
    width: 500px;
    height: auto;
    max-height: 350px;
    object-fit: cover;
    border-radius: 10px;
  }
  .arrow {
    font-size: 2rem;
    background: none;
    border: none;
    cursor: pointer;
    color: #555;
  }
  .arrow:hover {
    color: #222;
  }

  /* Dots */
  .dots {
    text-align: center;
    margin-top: 0.5rem;
  }
  .dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    margin: 0 4px;
    border-radius: 50%;
    background-color: #ccc;
  }
  .dot.active {
    background-color: #666;
  }
</style>
