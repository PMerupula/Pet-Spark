<!-- src/App.svelte -->
<script lang="ts">
    import Navbar from './components/Navbar.svelte';
    import Banner from './components/Banner.svelte';
    import PetDetails from './PetDetails.svelte';
</script>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
    }

    .main-wrapper {
        padding-top: 4.5rem;
    }
</style>

<Navbar />

<Banner />

<div class="main-wrapper">
    <PetDetails />
</div>
