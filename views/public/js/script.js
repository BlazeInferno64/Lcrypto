const img = document.querySelector(".img");
const downloadBtn = document.querySelector(".down");

img.addEventListener("contextmenu", (e) => {
    e.preventDefault();
})

let url;

const lcryptoURL = 'https://raw.githubusercontent.com/BlazeInferno64/Lcrypto/main/dist/Lcrypto.exe';
const lcryptoDecryptURL = 'https://raw.githubusercontent.com/BlazeInferno64/Lcrypto/main/dist/Lcrypto-decrypt.exe';

document.addEventListener("DOMContentLoaded", (e) => {
    console.log(`Welcome to Lcrypto's homepage!`)
})

const downloadFiles = () => {
    url = lcryptoURL;
    const aTag = document.createElement("a");
    aTag.href = url;
    aTag.download = "Lcrypto-main.exe";
    aTag.style.display = "none";
    document.body.appendChild(aTag);
    aTag.click();
    document.body.removeChild(aTag);
    console.log(`Successfully downloaded Lcrypto.exe!`);

    url = lcryptoDecryptURL;
    const aTag2 = document.createElement("a");
    aTag2.href = url;
    aTag.download = "Lcrypto-decrypt.exe";
    aTag2.style.display = "none";
    document.body.appendChild(aTag2);
    aTag2.click();
    document.body.removeChild(aTag2);
    console.log(`Successfully downloaded Lcrypto-decrypt.exe`);
}


downloadBtn.addEventListener("click",(e) => {
    downloadFiles();
})
