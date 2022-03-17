<script>
    
    export var arr_q;
    export var url;
    var answers = arr_q.filter(function(e){
        if(e == true)
            return e;
    });
    const indices = arr_q.reduce((out, bool, index) => bool ? out : out.concat(index),[])
    const q_a = async () => {
        const response = await fetch(url+"api/get_right_answ");
        const json = await response.json();
        return json;
    } 
    var q_A = q_a();  
</script>
  
<main>
    <p class = "cool">
        Ati raspuns la {answers.length}/{arr_q.length} intrebari. :D
    </p>
    {#if answers.length != 5}
        {#await q_A}
        ...loading answers
        {:then data}
            {#each indices as index }
            <div class="container">
                <p>{data.q[index]}</p>
                <p>{data.a[index]}</p>
               </div>
            {/each}   
        {/await}
    {/if}
</main>
<style>
   
.cool{
    font-family: 'Yeseva One', cursive;
    font-size: 2rem;
}

.container {
    display: block;
    position: relative;
    font-size: 1.3rem;
    margin: 10px;
    width: 550px;
    padding: 10px;
    font-family: 'Yeseva One', cursive;
}

</style>