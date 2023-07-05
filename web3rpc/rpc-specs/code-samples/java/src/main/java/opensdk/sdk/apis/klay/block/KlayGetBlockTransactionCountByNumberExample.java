package opensdk.sdk.apis.klay.block;

import opensdk.sdk.apis.constant.UrlConstants;
import org.web3j.protocol.klaytn.core.method.response.KlayGetBlockTransactionCountByNumberResponse;
import org.web3j.protocol.http.HttpService;
import org.web3j.protocol.klaytn.Web3j;

import java.io.IOException;

public class KlayGetBlockTransactionCountByNumberExample {

    private Web3j w3 = Web3j.build(new HttpService(UrlConstants.TEST_URL));

    void klayGetBlockTransactionCountByNumberExample() throws IOException {
        KlayGetBlockTransactionCountByNumberResponse gr = w3.klayGetBlockTransactionCountByNumber(
            "0xe8")
        .send();
        gr.getResult();
    }
}
