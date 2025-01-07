


function atualizar_data(){
    const formattedDate1 = new Intl.DateTimeFormat('pt-BR', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(new  Date());
    
    const datePDF = document.querySelector(".datePDF");
    datePDF.innerHTML += formattedDate1.replace('às', '-').replace('Às', '-');

    const formattedDate2 = new Intl.DateTimeFormat('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
    }).format(new  Date());

    const dateHeader = document.getElementById('data');
    dateHeader.innerHTML = formattedDate2;
}



const btnsave = document.querySelector("#save");
btnsave.addEventListener("click", function(){
    let ids = ['pedido', 'validade', 'vendedor', 'codigo-nome', 'cpf-cnpj', 'rg-ie', 'endereco', 'complemento', 'bairro', 'cidade-uf', 'cep', 'telefone', 'contato',  'celular','email'];

    for(let i = 0; i < ids.length; i++){
        let imput = document.getElementById(ids[i] + '-imput');
        let output = document.getElementById(ids[i]);

        if(imput){
            output.textContent = imput.value;
            console.log('execução: ' + `${i + 1}`);
        }
    }
});



// download pdf
const btnpdf = document.getElementById("download");
btnpdf.addEventListener("click", function(){
    
    let opt = {
        margin:       [0, 0, 0, 0],
        filename:     'myfile.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2},
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait'},
    };

    const element = document.getElementById('download-pdf');

    html2pdf().set(opt).from(element).save();
});

atualizar_data();
