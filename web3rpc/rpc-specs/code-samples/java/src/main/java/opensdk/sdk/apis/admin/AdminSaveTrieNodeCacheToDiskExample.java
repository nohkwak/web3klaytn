package opensdk.sdk.apis.admin;

import opensdk.sdk.apis.constant.UrlConstants;
import org.web3j.protocol.klaytn.core.method.response.AdminSaveTrieNodeCacheToDiskResponse;
import org.web3j.protocol.http.HttpService;
import org.web3j.protocol.klaytn.Web3j;

import java.io.IOException;

public class AdminSaveTrieNodeCacheToDiskExample {
    private Web3j w3 = Web3j.build(new HttpService(UrlConstants.TEST_URL));

    void adminSaveTrieNodeCacheToDiskExample() throws IOException {
        AdminSaveTrieNodeCacheToDiskResponse response = w3.adminSaveTrieNodeCacheToDisk().send();
        response.getResult();
    }
}
