// form submit
const form = document.getElementById("form");
const name_feld = document.getElementById("name");
const email = document.getElementById("email");
const message = document.getElementById("message");
const error_message = document.getElementById("error");
try {
  form.addEventListener("submit", (e) => {
    let messages = [];
    if (name_feld.value === "" || name_feld.value == null) {
      messages.push(" Name cannot be empty ");
      name_feld.style.borderColor = "red";
    }
    if (email.value === "" || email.value == null) {
      messages.push(" Email cannot be empty ");
      email.style.borderColor = "red";
    }
    if (message.value === "" || message.value == null) {
      messages.push(" Message cannot be empty ");
      message.style.borderColor = "red";
    }
    if (messages.length > 0) {
      e.preventDefault();
      error_message.innerText = messages.join(", ");
    }
  });
} catch (TypeErorr) {
  console.log("Wrong Page !");
}
const form_a = document.getElementById("form_a");
const first_name = document.getElementById("first_name");
const middle_name = document.getElementById("middle_name");
const last_name = document.getElementById("last_name");
const email_a = document.getElementById("email_a");
const phone = document.getElementById("phone");
const sector = document.getElementById("sector");
const type = document.getElementById("type");
const sex = document.getElementById("sex");
const submit = document.getElementById("submit");

const error_message_a = document.getElementById("error_a");

try {
  form_a.addEventListener("submit", (e) => {
    let messages = [];
    if (first_name.value === "" || first_name.value == null) {
      messages.push(" First name cannot be empty ");
      first_name.style.borderColor = "red";
    }
    if (middle_name.value === "" || middle_name.value == null) {
      messages.push(" Middle name cannot be empty ");
      middle_name.style.borderColor = "red";
    }
    if (last_name.value === "" || last_name.value == null) {
      messages.push(" Last name cannot be empty ");
      last_name.style.borderColor = "red";
    }
    if (email_a.value === "" || email_a.value == null) {
      messages.push(" Email cannot be empty ");
      email_a.style.borderColor = "red";
    }
    if (phone.value === "" || phone.value == null) {
      messages.push(" phone cannot be empty ");
      phone.style.borderColor = "red";
    }
    if (sector.value === "" || sector.value == null) {
      messages.push(" Deartment cannot be empty ");
      sector.style.borderColor = "red";
    }
    if (type.value === "" || phone.value == null) {
      messages.push(" Program type  cannot be empty ");
      type.style.borderColor = "red";
    }
    if (sex.value === "" || sex.value == null) {
      messages.push(" Sex feild cannot be empty ");
      sex.style.borderColor = "red";
    }
    if (messages.length > 0) {
      e.preventDefault();
      error_message_a.innerText = messages.join(", ");
    }
    if (messages.length > 4) {
      e.preventDefault();
      error_message_a.innerText = " Please make sure to fill all filds ";
    }
  });
} catch (TypeErorr) {
  console.log("Wrong Page");
}

function reveal() {
  reveals = document.querySelectorAll(".reveal");
  for (i = 0; i < reveals.length; i++) {
    let revealTop = reveals[i].getBoundingClientRect().top;
    revealPoint = 150;
    if (revealTop < window.innerHeight - revealPoint) {
      const cards = document.querySelectorAll(".reveal-element");
      cards.forEach((card) => {
        card.classList.add("active");
      });
    } else {
      const cards = document.querySelectorAll(".reveal-element");
      cards.forEach((card) => {
        card.classList.remove("active");
      });
    }
  }
}
reveal();
