<script>
    export var qa;
   
</script>

<main>

    {#await qa}
        ...loading
    {:then data} 
        {data}
    {/await}
</main>

<style>
    main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
    background-color: rgb(53, 53, 53);
  }
</style>