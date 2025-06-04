<script>
    export let username = "Petpet";
</script>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
    }

    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        background-color: #2196F3;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-sizing: border-box;
        z-index: 1000;
    }

    .spacer {
        height: 4.5rem;
    }

    .nav-left,
    .nav-right {
        display: flex;
        align-items: center;
    }

    .nav-left {
        gap: 0.5rem;
    }

    .nav-right {
        gap: 1rem;
    }

    .icon {
        font-size: 1.3rem;
        cursor: pointer;
    }
</style>

<div class="navbar">
    <div class="nav-left">
         <span>PetSpark</span>
    </div>
    <div class="nav-right">
        <span class="icon">🤍</span>
        <span>{username}</span>
    </div>
</div>
<div class="spacer"></div>
