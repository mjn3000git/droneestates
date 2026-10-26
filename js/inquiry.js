(function () {
  var form = document.getElementById("inquiry-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var btn = form.querySelector("button[type=submit]");
    btn.disabled = true;
    status.textContent = "Sending...";
    fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
      .then(function (r) {
        if (r.ok) { form.reset(); status.textContent = "Thank you. Your inquiry was sent, and we'll be in touch soon."; }
        else { status.textContent = "Sorry, something went wrong. Please try again."; }
      })
      .catch(function () { status.textContent = "Sorry, something went wrong. Please try again."; })
      .then(function () { btn.disabled = false; status.focus(); });
  });
})();
