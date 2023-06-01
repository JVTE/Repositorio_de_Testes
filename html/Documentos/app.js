window.onload = function(){
    var fileInput = document.getElementById('file-upload');
    var documentList = document.getElementById('document-list')
    
    fileInput.addEventListener('change', function (event) {  
        var file = event.target.files[0];
        var listItem = document.createElement('li');
        var link = document.createElement('a');
        link.href = URL.createObjectURL(file);
        link.innerHTMLText = file.name;
        listItem.appendChild(link);
        documentList.appendChild(listItem);
    });
}