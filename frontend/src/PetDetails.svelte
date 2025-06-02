<script lang="ts">
  import Navbar from './components/Navbar.svelte';
  import Banner from './components/Banner.svelte';
  import PetCard from './components/PetCard.svelte';

  const pet = {
    name: "Raja",
    location: "Davis, CA",
    age: "Young",
    gender: "Male",
    color: "Tricolor (Brown, Black, & White)",
    houseTrained: "Yes",
    health: "Vaccinations up to date, spayed / neutered.",
    about: `Hi I'm Raja! I am a cuddle bug who just wants to lay in your lap and snuggle all day and gets lots of love and attention...`,
    imageUrl: "https://placekitten.com/400/300"
  };
</script>

<Navbar />
<Banner />

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
