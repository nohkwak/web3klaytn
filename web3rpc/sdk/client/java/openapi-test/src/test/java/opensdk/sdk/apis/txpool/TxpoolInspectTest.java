package opensdk.sdk.apis.txpool;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;

import opensdk.sdk.apis.constant.UrlConstants;
import org.web3j.protocol.klaytn.core.method.response.TxpoolInspectResponse;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.web3j.protocol.http.HttpService;
import org.web3j.protocol.klaytn.Web3j;

import java.io.IOException;

@DisplayName("Txpool RPC Test")
public class TxpoolInspectTest {
    private Web3j w3 = Web3j.build(new HttpService(UrlConstants.SERVER_URL));

    @Test
    @DisplayName("RPC txpool_inspect")
    void whenRequestValid_ThenCall200ResponseReturns() throws IOException {
        TxpoolInspectResponse response = w3.txpoolInspect().send();
        assertNotNull(response);
        assertNull(response.getError());
    }
}
