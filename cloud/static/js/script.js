const dots = document.querySelectorAll(".dot");
const textFields = document.querySelectorAll(".text-field");

dots.forEach(dot => {
  dot.addEventListener("click", event => {
    const dotId = event.target.id;
    const textFieldId = `text-field${dotId.charAt(dotId.length - 1)}`;
    textFields.forEach(textField => {
      if (textField.id === textFieldId) {
        textField.style.display = "block";
      } else {
        textField.style.display = "none";
      }
    });
  });
});