<script>
  export let name;
  export let location;
  export let age;
  export let gender;
  export let color;
  export let houseTrained;
  export let health;
  export let about;
  export let imageUrl = '';
</script>

<style>
  .container {
    display: flex;
    flex-wrap: wrap;
    background: white;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    width: calc(100% - 2rem);
    max-width: 960px;
    margin: 2rem auto;
    align-items: flex-start;
    gap: 2rem;
    box-sizing: border-box;
  }

  .left {
    flex-shrink: 0;
  }

  .pet-img {
    width: 240px; 
    height: auto;
    border-radius: 10px;
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
  }

  .like-btn {
    margin-top: 1rem;
    background-color: #2196F3;
    border: none;
    border-radius: 50px;
    padding: 0.6rem 1.2rem;
    color: white;
    font-size: 1.4rem;
    cursor: pointer;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .right {
    flex: 1;
    text-align: left;
  }

  .right h2 {
    margin-bottom: 1rem;
  }

  .right p {
    margin: 0.4rem 0;
    line-height: 1.4;
  }

  .about {
    margin-top: 1rem;
  }
</style>

<div class="container">
  <div class="left">
    <img src={imageUrl} alt="Pet image" class="pet-img" />
  </div>

  <div class="right">
    <h2>{name}</h2>
    <p><strong>Location:</strong> {location}</p>
    <p><strong>Age:</strong> {age}</p>
    <p><strong>Gender:</strong> {gender}</p>
    <p><strong>Color:</strong> {color}</p>
    <p><strong>House-trained:</strong> {houseTrained}</p>
    <p><strong>Health:</strong> {health}</p>

    <div class="about">
      <p><strong>About me:</strong></p>
      <p>{about}</p>
    </div>
  </div>
</div>
