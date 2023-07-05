package opensdk.sdk.apis.klay.configuration;

import opensdk.sdk.apis.constant.UrlConstants;
import org.web3j.protocol.klaytn.core.method.response.KlayClientVersionResponse;
import org.web3j.protocol.http.HttpService;
import org.web3j.protocol.klaytn.Web3j;

import java.io.IOException;

public class KlayClientVersionExample {

    private Web3j w3 = Web3j.build(new HttpService(UrlConstants.TEST_URL));

    void klayClientVersionExample() throws IOException {
        KlayClientVersionResponse cr = w3.klayClientVersion().send();
        cr.getResult();
    }
}
