<script>
  export let name;
  const url="http://localhost:8081/api/register_answ"
  let firstIncAnswer = "";
  let firstName = ""
  let lastName = ""
  let q1 = true;
  let q2 = true;
  let q3 = true;
  let q4 = true;
  let q5 = true;
  const send_answ = (qA) => {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify(qA));
  }
  const check_answers = () => {
	firstIncAnswer = ""; 
    q1 = document.getElementById("1-option").checked;
    q2 = document.getElementById("22-option").checked;
    q3 = document.getElementById("444-option").checked;
    q4 = document.getElementById("2222-option").checked;
    q5 = document.getElementById("33333-option").checked;
	if(!q1 && firstIncAnswer == ""){
		firstIncAnswer = "q1"
	}
	if(!q2 && firstIncAnswer == ""){
		firstIncAnswer = "q2"
	}
	if(!q3 && firstIncAnswer == ""){
		firstIncAnswer = "q3"
	}
	if(!q4 && firstIncAnswer == ""){
		firstIncAnswer = "q4"
	}
	if(!q5 && firstIncAnswer == ""){
		firstIncAnswer = "q5"
	}
	const qA={
		q1: q1,
		q2: q2,
		q3: q3,
		q4: q4,
		q5: q5,
		firstName: firstName,
		lastName: lastName
	}
	//console.log(qA);
	send_answ(qA);
	//console.log(firstIncAnswer);
  };
</script> 

<main>
  <h1>Quiz {name}</h1>
  <div class="container">
	<label for="nume" class="numelabel">Nume</label>
	<input type="text" class="nume" id="firstName"  bind:value={firstName} placeholder="Nume"/>
	<label for="prenume" class="numelabel">Prenume</label>
	<input type="text" class="nume" id="lastName"  bind:value={lastName} placeholder="Prenume"/>
  </div>
  <div class="container" id="q1">
    <h3>1. Care dintre figurile de mai jos este o poarta AND?</h3>

    <ul>
      <li>
        <input type="radio" id="1-option" name="selector1" />
        <label for="1-option"
          ><img src="quizes/q1/and.png" alt="and gate" /></label
        >

        <div class="check" />
      </li>

      <li>
        <input type="radio" id="2-option" name="selector1" />

        <label for="2-option"
          ><img src="quizes/q1/or.png" alt="or gate" /></label
        >

        <div class="check"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="3-option" name="selector1" />
        <label for="3-option"
          ><img src="quizes/q1/xor.png" alt="xor gate" /></label
        >

        <div class="check"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="4-option" name="selector1" />
        <label for="4-option"
          ><img src="quizes/q1/not.png" alt="not gate" /></label
        >

        <div class="check"><div class="inside" /></div>
      </li>
    </ul>
    {#if !q1}
      <p class="incorrect">
        Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
      </p>
    {/if}
  </div>

  <div class="container" id="q2">
    <h3>2. Un MUX 4:1 reprezinta un circuit cu:</h3>

    <ul>
      <li>
        <input type="radio" id="11-option" name="selector11" />
        <label for="11-option">1 intrare si 4 iesiri</label>

        <div class="check1" />
      </li>

      <li>
        <input type="radio" id="22-option" name="selector11" />
        <label for="22-option">4 intrari si 1 iesire</label>

        <div class="check1"><div class="inside" /></div>
      </li>
    </ul>
    {#if !q2}
      <p class="incorrect">
        Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
      </p>
    {/if}
  </div>

  <div class="container" id="q3">
    <h3>3. Ce operatie logica indeplineste poarta XOR?</h3>

    <ul>
      <li>
        <input type="radio" id="111-option" name="selector111" />
        <label for="111-option">Suma</label>

        <div class="check1" />
      </li>

      <li>
        <input type="radio" id="222-option" name="selector111" />
        <label for="222-option">Scadere</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="333-option" name="selector111" />
        <label for="333-option">Inmultimre</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="444-option" name="selector111" />
        <label for="444-option">Suma modulo 2</label>

        <div class="check1"><div class="inside" /></div>
      </li>
    </ul>
    {#if !q3}
      <p class="incorrect">
        Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
      </p>
    {/if}
  </div>

  <div class="container" id="q4">
    <h3>
      4. Selectati care dintre urmatoarele variante reprezinta functia logica a
      portii OR?
    </h3>

    <ul>
      <li>
        <input type="radio" id="1111-option" name="selector1111" />
        <label for="1111-option">a & b</label>

        <div class="check1" />
      </li>

      <li>
        <input type="radio" id="2222-option" name="selector1111" />
        <label for="2222-option">a | b</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="3333-option" name="selector1111" />
        <label for="3333-option">a ^ b</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="4444-option" name="selector1111" />
        <label for="4444-option">a % b</label>

        <div class="check1"><div class="inside" /></div>
      </li>
    </ul>
    {#if !q4}
      <p class="incorrect">
        Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
      </p>
    {/if}
  </div>
  <div class="container" id="q5">
    <h3>5. Ce varianta de mai jos reprezinta operatia corecta a portii AND?</h3>

    <ul>
      <li>
        <input type="radio" id="11111-option" name="selector11111" />
        <label for="11111-option">1 & 0 = 1</label>

        <div class="check1" />
      </li>

      <li>
        <input type="radio" id="22222-option" name="selector11111" />
        <label for="22222-option">1 | 1 = 1</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="33333-option" name="selector11111" />
        <label for="33333-option">1 & 1 = 1</label>

        <div class="check1"><div class="inside" /></div>
      </li>

      <li>
        <input type="radio" id="44444-option" name="selector11111" />
        <label for="44444-option">0 & 0 = 1</label>

        <div class="check1"><div class="inside" /></div>
      </li>
    </ul>
    {#if !q5}
      <p class="incorrect">
        Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
      </p>
    {/if}
  </div>
  <button on:click={check_answers}>
    <a href="#{firstIncAnswer}" class="buttons flatbutt orange">Submit quiz</a>
  </button>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
    background-color: rgb(53, 53, 53);
  }

  h1 {
    display: block;
    position: relative;
    margin: 30px auto;
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
    margin: 30px auto;
    height: auto;
    width: 800px;
    padding: 10px;
  }

  .incorrect {
    color: #ff0000;
    position: relative;
    font-weight: 300;
    font-size: 2em;
    padding: 15px;
  }

  button {
    background-color: transparent;
    background-repeat: no-repeat;
    border: none;
    cursor: pointer;
    overflow: hidden;
    outline: none;
  }

  .buttons {
    margin: 20px 10px 20px 10px;
    display: block;
    text-align: center;
    font-weight: 500;
    padding: 12px 20px 12px 20px;
    width: 300px;
    margin: auto;
  }

  a.flatbutt {
    background: #e26c3d;
    border-radius: 3px;
    color: rgb(0, 0, 0);
    font-size: 90%;
  }

  .orange {
    background: #f39c12;
  }

  h3 {
    color: #e2f8a5;
    text-transform: uppercase;
    font-size: 2em;
    font-weight: bold;
  }

  img {
    margin-top: 5px;
    margin-left: 15px;
    margin-right: auto;
    width: 50%;
    margin-bottom: 10px;
  }
  label img {
    width: 200px;
    height: 100px;
  }

  .container {
    display: block;
    position: relative;
    margin: 30px auto;
    height: auto;
    width: 800px;
    padding: 10px;
  }
  .container .nume{
	  display: block;
	  margin: 30px auto;
	  border-radius: 15px;
	  width: 600px;
     height: 70px;
  }
  .container .numelabel{
	  color: aliceblue;
	  font-size: 1.65rem;

  }

  .container ul {
    list-style: none;
    margin: 0;
    padding: 0;
    overflow: auto;
  }

  ul li {
    color: #aaaaaa;
    display: block;
    position: relative;
    float: left;
    width: 100%;
    height: 100px;
    border-bottom: 1px solid rgb(0, 0, 0);
    height: auto;
    border-width: 0.2rem;
  }

  ul li input[type="radio"] {
    position: absolute;
    visibility: hidden;
  }

  ul li label {
    display: block;
    position: relative;
    font-weight: 300;
    font-size: 2em;
    padding: 25px 25px 25px 80px;
    color: #ffffff;
    z-index: 9;
    cursor: pointer;
  }

  ul li:hover label {
    color: #0dff92;
  }

  ul li .check {
    display: block;
    position: absolute;
    border: 5px solid #aaaaaa;
    border-radius: 100%;
    height: 25px;
    width: 25px;
    top: 65px;
    left: 20px;
    z-index: 5;
    transition: border 0.25s linear;
    -webkit-transition: border 0.25s linear;
  }

  ul li .check1 {
    display: block;
    position: absolute;
    border: 5px solid #aaaaaa;
    border-radius: 100%;
    height: 25px;
    width: 25px;
    top: 33px;
    left: 20px;
    z-index: 5;
    transition: border 0.25s linear;
    -webkit-transition: border 0.25s linear;
  }

  ul li:hover .check {
    border: 5px solid #0dff92;
  }

  ul li .check::before {
    display: block;
    position: absolute;
    content: "";
    border-radius: 100%;
    height: 15px;
    width: 15px;
    top: 5px;
    left: 5px;
    margin: auto;
  }

  input[type="radio"]:checked ~ .check {
    border: 5px solid #0dff92;
  }

  input[type="radio"]:checked ~ .check::before {
    background: #0dff92;
  }

  ul li:hover .check1 {
    border: 5px solid #0dff92;
  }

  ul li .check1::before {
    display: block;
    position: absolute;
    content: "";
    border-radius: 100%;
    height: 15px;
    width: 15px;
    top: 5px;
    left: 5px;
    margin: auto;
  }

  input[type="radio"]:checked ~ .check1 {
    border: 5px solid #0dff92;
  }

  input[type="radio"]:checked ~ .check1::before {
    background: #0dff92;
  }

  input[type="radio"]:checked ~ label {
    color: #0dff92;
  }

  @media (min-width: 840px) {
    main {
      max-width: none;
    }
  }
</style>
