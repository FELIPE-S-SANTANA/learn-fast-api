async function carregarAnimais(){
    const response = await axios.get('http://localhost:8000/animais')
    const animais =  response.data
    const lista = document.getElementById('lista_animais')
    
    animais.forEach(animal => {
        const item = document.createElement('li')
        item.innerText = animal.nome
        lista.appendChild(item)
    });
     
}   

function cadastrarAnimais(){
    const form_animal = document.getElementById('form_animal')
    const input_nome = document.getElementById('nome')
    form_animal.onsubmit = async(event)=>{
        event.preventDefault()
        const nome_animal = input_nome.value
        alert(`submit chamado...${nome_animal}`)

        await axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: 4,
            sexo: 'femea',
            cor: 'preto'
        })
    }

}

function app(){
    console.log("app iniciada")
    carregarAnimais()
    cadastrarAnimais()
}

app()