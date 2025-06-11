<!-- src/routes/petdetails/+page.svelte -->

<script lang="ts">
    import { page } from '$app/stores'
    import PetCard from '../../../components/PetCard.svelte';
    import PetGrid from '../../../components/PetGrid.svelte';

    const pets = [
        {
            id: 1,
            name: "Raja",
            location: "Davis, CA",
            age: "Young",
            gender: "Male",
            color: "Tricolor (Brown, Black, & White)",
            houseTrained: "Yes",
            health: "Vaccinations up to date, spayed / neutered.",
            about: `Hi I'm Raja! …`,
            imageUrl: "https://placekitten.com/300/400"
        },
    ];
    const id = Number($page.params.id);

    const pet = pets.find(p => p.id === id);

</script>

<style>
    .container {
        max-width: 960px;
        margin: 2rem auto;
    }

    .recommend-title {
        margin: 2rem 0 1rem;
        font-size: 1.5rem;
        color: #333;
        text-align: center;
    }
</style>

<div class="container">
    {#if pet}
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
    {:else}
    <p>Pet not found</p>
    {/if}

    <div class="recommend-title">Recommended Pets for You</div>

    <PetGrid />
</div>
