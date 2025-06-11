<script>
    export let pets = [];
    let index = 0;

    function swipeLike() {
        console.log("Liked", pets[index]);
        index++;
    }

    function swipePass() {
        console.log("Passed", pets[index]);
        index++;
    }
</script>

{#if pets[index]}
    <div class="card">
        <img src={pets[index].image} alt={pets[index].name} />
        <h2>{pets[index].name}</h2>
        <p>{pets[index].age} years old</p>
        <div class="actions">
            <button on:click={swipePass}>❌ Pass</button>
            <button on:click={swipeLike}>✅ Like</button>
        </div>
    </div>
{:else}
    <p>No more cats to show!</p>
{/if}

<style>
    .card {
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        max-width: 400px;
        margin: 2rem auto;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    img {
        width: 100%;
        border-radius: 8px;
    }

    .actions {
        margin-top: 1rem;
        display: flex;
        justify-content: space-around;
    }

    button {
        padding: 0.5rem 1rem;
        font-size: 1.1rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
</style>
