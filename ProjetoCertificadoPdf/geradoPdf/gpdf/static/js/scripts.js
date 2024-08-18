function formataCPF(input) {
    let value = input.value.replace(/\D/g, '');  
    value = value.replace(/(\d{3})(\d)/, '$1.$2');  
    value = value.replace(/(\d{3})(\d)/, '$1.$2');  
    value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');  

    input.value = value;
}

function formataRG(input) {
    let value = input.value.replace(/\D/g, '');  
    value = value.replace(/(\d{2})(\d)/, '$1.$2');  
    value = value.replace(/(\d{3})(\d)/, '$1.$2');  
    value = value.replace(/(\d{3})([\dXx])$/, '$1-$2');  

    input.value = value.toUpperCase();  
}