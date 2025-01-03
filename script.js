const datePDF = document.querySelector(".datePDF");

const formattedDate = new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
}).format(new  Date());;

datePDF.innerHTML += formattedDate.replace('às', '-').replace('Às', '-');





// download pdf
const btnpdf = document.querySelector("#download");

btnpdf.addEventListener("click", function(){
    
    let opt = {
        margin:       0,
        filename:     'myfile.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait', moveTo: '100, 100' },
        moveto: {
            top: 10,
            left: 10
        }
    };

    const element = document.querySelector('#test');

    html2pdf().set(opt).from(element).save();
});

