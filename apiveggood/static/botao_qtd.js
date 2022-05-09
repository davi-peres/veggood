const soma = document.querySelector(".add-qtd"),
    subtrai = document.querySelector(".subtrai-qtd"),
    num = document.querySelector(".num");

    let a = 1;
    soma.addEventListener("click", () => {
        a++;
        a = (a < 10) ? "0" + a : a;
        num.innerText = a;
    })

    subtrai.addEventListener("click", () => {
        if (a > 1) {
            a -= 1;
            a = (a < 10) ? "0" + a : a;
            num.innerText = a;
        }
    })
