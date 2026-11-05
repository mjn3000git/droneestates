(function () {
  var form = document.getElementById("build-form");
  if (!form) return;
  var $ = function (s) { return form.querySelectorAll(s); };
  var money = function (n) { return "$" + n.toLocaleString("en-US"); };
  var estEl = document.getElementById("est"), linesEl = document.getElementById("lines");
  var summaryIn = document.getElementById("package_summary"), rangeIn = document.getElementById("estimate_range");
  var status = document.getElementById("build-status");

  function calc() {
    var lines = [], lo = 0, hi = 0, quote = false;
    var pkg = form.querySelector("input[name=package]:checked");
    var plo = +pkg.dataset.lo, phi = +pkg.dataset.hi;
    lo += plo; hi += phi;
    lines.push([pkg.value, plo === phi ? money(plo) : money(plo) + " to " + money(phi)]);
    var zoneSel = document.getElementById("zone"), zoneOpt = zoneSel.options[zoneSel.selectedIndex];
    var travel = +zoneSel.value;
    $("input[type=number]").forEach(function (i) {
      var q = Math.max(0, Math.min(+i.max || 99, Math.floor(+i.value || 0)));
      if (!q) return;
      var each = +i.dataset.each + (i.dataset.travel ? travel : 0);
      lo += each * q; hi += each * q;
      lines.push([i.dataset.name + " x " + q + (i.dataset.travel && travel ? " (incl. travel)" : ""), money(each * q)]);
    });
    $("input[type=checkbox][data-name]").forEach(function (c) {
      if (!c.checked) return;
      lo += +c.dataset.lo; hi += +c.dataset.hi;
      lines.push([c.dataset.name, money(+c.dataset.lo)]);
    });
    var lm = document.getElementById("landmap");
    if (lm.value === "quote") { quote = true; lines.push(["Land map, over 50 acres", "By quote"]); }
    else if (lm.value) { lo += +lm.value; hi += +lm.value; lines.push(["Land map, " + lm.options[lm.selectedIndex].text.split(",")[0].toLowerCase(), money(+lm.value)]); }
    lo += travel; hi += travel;
    lines.push(["Travel: " + zoneOpt.dataset.name, travel ? money(travel) : "No charge"]);
    var del = form.querySelector("input[name=delivery]:checked"), fee = +del.dataset.fee;
    lo += fee; hi += fee;
    lines.push(["Delivery: " + del.value, fee ? money(fee) : "Included"]);
    var range = (lo === hi ? money(lo) : money(lo) + " to " + money(hi)) + (quote ? " plus land map by quote" : "");
    estEl.textContent = range;
    linesEl.innerHTML = "";
    lines.forEach(function (l) {
      var li = document.createElement("li"), a = document.createElement("span"), b = document.createElement("b");
      a.textContent = l[0]; b.textContent = l[1]; li.appendChild(a); li.appendChild(b); linesEl.appendChild(li);
    });
    summaryIn.value = lines.map(function (l) { return l[0] + ": " + l[1]; }).join("\n");
    rangeIn.value = range;
  }
  form.addEventListener("input", calc);
  form.addEventListener("change", calc);
  calc();

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    calc();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var btn = form.querySelector("button[type=submit]");
    btn.disabled = true;
    status.textContent = "Sending...";
    var fd = new FormData();
    ["_gotcha", "_subject", "name", "email", "phone", "preferred_dates", "property_address", "notes", "package", "delivery"].forEach(function (k) {
      var el = form.elements[k]; if (el) fd.append(k, el.value);
    });
    fd.append("travel_zone", document.getElementById("zone").selectedOptions[0].dataset.name);
    fd.append("estimate_range", rangeIn.value);
    fd.append("package_summary", summaryIn.value);
    fetch(form.action, { method: "POST", body: fd, headers: { Accept: "application/json" } })
      .then(function (r) {
        if (!r.ok) throw new Error();
        form.closest("section").hidden = true;
        var t = document.getElementById("thanks"); t.hidden = false;
        t.scrollIntoView(); t.querySelector("h2").setAttribute("tabindex", "-1"); t.querySelector("h2").focus();
      })
      .catch(function () { status.textContent = "Sorry, something went wrong. Please try again."; btn.disabled = false; status.focus(); });
  });
})();
