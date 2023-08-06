function initCKEditor(id) {
  console.log(id);
  ClassicEditor
    .create(document.getElementById(id))
    .catch(error => {
      console.error(error);
    });

}
