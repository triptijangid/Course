// Skeleton — fill in the logic for each key
document.addEventListener("keydown", function (e) {
  const secA = document.querySelector("#sec-A");
  const secB = document.querySelector("#sec-B");
  const secC = document.querySelector("#sec-C");
  const secD = document.querySelector("#sec-D");

  if (e.key === "a") {
    // scroll to sec-A
    secA.scrollIntoView()
  } else if (e.key === "b") {
    // scroll to sec-B
    secB.scrollIntoView()
  } else if (e.key === "c") {
    // scroll to sec-C
    secC.scrollIntoView()
  } else if (e.key === "d") {
    // scroll to sec-D
    secD.scrollIntoView()
  } else if (e.key === "t" || e.key === "T") {
    // scroll to top
    document.documentElement.scrollTop = document.documentElement.scrollHeight
  } else if (e.key === "x" || e.key === "X") {
    // create Dismiss button, append to body, remove after 3s
    const btn = document.createElement("button");
    btn.innerText = "Dismiss";
    document.body.appendChild(btn);

    setTimeout(() => {
      btn.remove();
    }, 3000);
  }
});
