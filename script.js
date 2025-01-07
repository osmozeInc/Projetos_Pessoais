// função para receber a data do dia e atualizar no documento
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


// função para fazer o download do pdf
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


// função para atualizar o pdf pelo formulário
const btnsave = document.querySelector("#save");
btnsave.addEventListener("click", function(){

    // nome dos ids do formulário foi separado em vários arrays para facilitar a leitura e correção

    // repetições para alterar o pdf de acordo com cada id

    // repetição da tabela 1
    for(let i = 0; i < 15; i++){
        
        let tab1_ids = ['pedido', 'validade', 'vendedor', 'codigo-nome', 'cpf-cnpj', 'rg-ie', 'endereco', 'complemento', 'bairro', 'cidade-uf', 'cep', 'telefone', 'contato',  'celular', 'email'];

        let imput = document.getElementById(tab1_ids[i] + '-input');
        let output = document.getElementById(tab1_ids[i]);

        if(imput){
            output.textContent = imput.value;
        }
        else{
            console.log('tab1 - erro com o input' + tab1_ids[i]);
        }
    }

    
    // repetição da tabela 2
    for(let i = 0; i < 6; i++){

        let tab2_ids = ['codigo', 'nome-produto', 'quantidade', 'un', 'vlr-unit', 'vlr-sub-total'];

        let imput = document.getElementById(tab2_ids[i] + '-input');
        let output = document.getElementById(tab2_ids[i]);

        if(imput){
            output.textContent = imput.value;
        }
        else{
            console.log('tb2 - erro com o input' + tab2_ids[i]);
        }
    }


    // repetição da tabela 3
    for(let i = 0; i < 10; i++){

        let tab3_4_5_ids = ['observacoes', 'qtde-itens', 'qtde-total', 'sub-total', 'frete', 'seguro', 'outros', 'desconto', 'total', 'condicoes-pagamento'];

        let imput = document.getElementById(tab3_4_5_ids[i] + '-input');
        let output = document.getElementById(tab3_4_5_ids[i]);

        if(imput){
            output.textContent = imput.value;
        }
        else{
            console.log('tab345 - erro com o input' + tab3_4_5_ids[i]);
        }
    }
});




atualizar_data();
