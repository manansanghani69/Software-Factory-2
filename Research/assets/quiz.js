(() => {
  const qs = document.querySelectorAll(".quiz-question");
  qs.forEach((q) => {
    const opts = q.querySelectorAll(".opt");
    const fb = q.querySelector(".quiz-feedback");
    const correct = q.querySelector("button.opt[data-correct='true']");
    opts.forEach((o) => {
      o.addEventListener("click", () => {
        if (o.classList.contains("locked")) return;
        opts.forEach((x) => x.classList.add("locked"));
        const isRight = o === correct;
        opts.forEach((x) => x.classList.add(isRight && x === correct ? "correct" : x === correct && !isRight ? "correct" : "wrong"));
        if (isRight) {
          o.classList.remove("wrong");
          o.classList.add("correct");
        }
        fb.classList.add("show", isRight ? "ok" : "no");
        fb.textContent = isRight
          ? (q.dataset.whyRight || "Correct.")
          : (q.dataset.whyWrong || "Not quite — reread the section above, then try again.");
      });
    });
  });
})();