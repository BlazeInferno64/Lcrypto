const img = document.querySelector(".img");
const downloadBtn = document.querySelector(".down");

img.addEventListener("contextmenu", (e) => {
    e.preventDefault();
})

document.addEventListener("DOMContentLoaded", (e) => {
    console.log(`Welcome to Lcrypto's homepage!`)
})

const downloadLcrypto = async() => {
    alert(`Downloaing Lcrypto.exe...`);
    window.location.href = `https://raw.githubusercontent.com/BlazeInferno64/Lcrypto/main/dist/Lcrypto.exe`;
}

downloadBtn.addEventListener("click",(e) => {
    downloadLcrypto().then(() => {
        alert(`Downloading Lcrypto-decrypt.exe...`);
        window.location.href = "https://raw.githubusercontent.com/BlazeInferno64/Lcrypto/main/dist/Lcrypto-decrypt.exe"
    })
})
