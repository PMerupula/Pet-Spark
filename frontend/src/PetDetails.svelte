<!-- src/PetDetails.svelte -->
<script lang="ts">
    import PetCard from './components/PetCard.svelte';
    import PetGrid from './components/PetGrid.svelte';

    const pet = {
        name: "Raja",
        location: "Davis, CA",
        age: "Young",
        gender: "Male",
        color: "Tricolor (Brown, Black, & White)",
        houseTrained: "Yes",
        health: "Vaccinations up to date, spayed / neutered.",
        about: `Hi I'm Raja! I am a cuddle bug who just wants to lay in your lap and snuggle all day and gets lots of love and attention.
    I am around 9 months old. I am still "working" in class until the end of February but make your appointment now to come visit me
    and get your application in now so I can come live with you and be forever in your home and in your heart!`,
        imageUrl: "https://placekitten.com/300/400"
    };
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

    <div class="recommend-title">Recommended Pets for You</div>

    <PetGrid />
</div>
