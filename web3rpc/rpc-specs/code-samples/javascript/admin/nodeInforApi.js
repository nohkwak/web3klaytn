const { JsonRpcProvider } = require("@klaytn/ethers-ext");
(() => {
  const provider = new JsonRpcProvider("https://public-en-baobab.klaytn.net");
  provider.admin
    .nodeInfo({}, (err, data, response) => {})
    .then((data) => {
      console.log(data);
    });
})();
