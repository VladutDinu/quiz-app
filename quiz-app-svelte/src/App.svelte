<script>
  export let name;
  import WrongAnswers from "./WrongAnswers.svelte";
  import { writable } from 'svelte/store';
  import Modal, { bind } from 'svelte-simple-modal';
  import Popup from './Popup.svelte';
  const modal = writable(null);
  const showModal = (arr_q, url) => modal.set(bind(Popup, { arr_q : arr_q, url : url }));
  const url="http://localhost:8081/"
  const q_a = async () => {
    const response = await fetch(url+"api/get_q");
    const json = await response.json();
    return json;
  }

  var q_A = q_a();

  let firstName = ""
  let lastName = ""
  let q1 = true;
  let q2 = true;
  let q3 = true;
  let q4 = true;
  let q5 = true;
  var arr_q = [q1,q2,q3,q4,q5];
  const send_answ = (qA) => {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url+"api/register_answ", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify(qA));
  }
  const check_answers = () => {

    q1 = document.getElementById("1-option").checked;
    q2 = document.getElementById("22-option").checked;
    q3 = document.getElementById("444-option").checked;
    q4 = document.getElementById("2222-option").checked;
    q5 = document.getElementById("33333-option").checked;
	
	const qA={
		q1: q1,
		q2: q2,
		q3: q3,
		q4: q4,
		q5: q5,
		firstName: firstName,
		lastName: lastName
	}
  arr_q = [q1,q2,q3,q4,q5];
	//console.log(qA);
	send_answ(qA);
	//console.log(firstIncAnswer);
  console.log(qA);
  console.log(arr_q);
  showModal(arr_q, url);
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

  
  
  {#await q_A}
	<p>...waiting</p>
  {:then data}
    {#each Array(data.q.length) as _,i }
    <div class="container" id="q{i+2}">
      <h3>{data.q[i]}</h3>
      <ul>
        {#each Array(data.a[i].length) as _,j }
          <li>
            <input type="radio" id="{(j+1).toString().repeat(i+2)}-option" name="selector{(2).toString().repeat(i+1)}" />
               <label for="{(j+1).toString().repeat(i+2)}-option">{data.a[i][j]}</label>
            <div class="check1"></div>
          </li>
          {/each}
        </ul>
      <!-- {#if !arr_q[i+1]}
        <p class="incorrect">
          Raspunsul oferit nu este corect, va rugam sa revizuiti intrebarea.
        </p>
      {/if} -->
   </div>
    {/each}
  {:catch error}
    <p style="color: red">{error.message}</p>
  {/await}

  
  <button on:click={check_answers}>
    <!-- svelte-ignore a11y-invalid-attribute -->
    <a href="#" class="buttons flatbutt orange">Submit quiz</a>
  </button>
  <Modal
  show={$modal}
  styleBg={{ backgroundColor: 'rgba(255, 255, 255, 0.85)' }}
  styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
>
  <button on:click={showModal}>Show modal</button>
</Modal>
  <WrongAnswers bind:qa={q_A} ></WrongAnswers>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
    background-color: rgb(53, 53, 53);
    font-family: 'Yeseva One', cursive;
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
    top: 25px;
    left: 25px;
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