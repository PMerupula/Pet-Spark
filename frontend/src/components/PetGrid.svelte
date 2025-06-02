<script>
    const allPets = [
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494949/dog.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494948/cat.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494950/rabbit.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494949/dog.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494948/cat.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494950/rabbit.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494949/dog.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494948/cat.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494950/rabbit.svg" },
        { name: "Pet Name", icon: "https://www.svgrepo.com/show/494949/dog.svg" }
    ];

    const itemsPerPage = 8;
    let currentPage = 0;

    $: visiblePets = allPets.slice(currentPage * itemsPerPage, (currentPage + 1) * itemsPerPage);

    function nextPage() {
        if ((currentPage + 1) * itemsPerPage < allPets.length) {
            currentPage++;
        }
    }

    function prevPage() {
        if (currentPage > 0) {
            currentPage--;
        }
    }
</script>

<style>
    .wrapper {
        width: calc(100% - 2rem);
        max-width: 960px;
        margin: 2rem auto;
        position: relative;
        box-sizing: border-box;
    }

    .arrow {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2rem;
        cursor: pointer;
        user-select: none;
        z-index: 10;
    }

    .arrow.disabled {
        color: #ddd;
        cursor: default;
    }

    .arrow.left {
        left: -1.5rem;
    }

    .arrow.right {
        right: -1.5rem;
    }

    /* 网格：两行四列 */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(2, auto);
        gap: 1rem;
    }

    .pet-card {
        background: white;
        border-radius: 10px;
        text-align: center;
        padding: 1rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        position: relative;
        transition: transform 0.2s ease;
    }

    .pet-card:hover {
        transform: translateY(-4px);
    }

    .pet-icon {
        width: 60px;
        height: 60px;
        margin-bottom: 0.5rem;
    }

    .heart {
        position: absolute;
        top: 8px;
        right: 8px;
        font-size: 1.2rem;
        color: #ccc;
        cursor: pointer;
    }

    .heart:hover {
        color: red;
    }

    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: #999;
        margin-top: 2rem;
    }
</style>

<div class="wrapper">
    <span class="arrow left {currentPage === 0 ? 'disabled' : ''}" on:click={prevPage}>
    ←
  </span>

    <span
            class="arrow right {(currentPage + 1) * itemsPerPage >= allPets.length ? 'disabled' : ''}"
            on:click={nextPage}
    >
    →
  </span>

    <div class="grid">
        {#each visiblePets as pet}
            <div class="pet-card">
                <div class="heart">♡</div>
                <img class="pet-icon" src={pet.icon} alt="icon" />
                <p>{pet.name}</p>
            </div>
        {/each}
    </div>

    <div class="footer">
        Copyright © 2025 UC Davis ECS 162
    </div>
</div>
