package opensdk.sdk.apis.klay.block;

import opensdk.sdk.models.KlayGetBlockWithConsensusInfoByNumberRangeResponse;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.klaytn.OpenSDK;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertNotNull;


public class KlayGetBlockWithConsensusInfoByNumberRangeTest {
    private final OpenSDK sdk = new OpenSDK("https://api.baobab.klaytn.net:8651");

    @Test
    @DisplayName("RPC klay_getBlockWithConsensusInfoByNumberRange")
    void whenRequestValid_ThenCall200ResponseReturns() throws IOException {
        Integer blockNumber = 1;
        Integer numberRange = 1;
        KlayGetBlockWithConsensusInfoByNumberRangeResponse response = sdk.klay
                .getBlockWithConsensusInfoByNumberRange(blockNumber , numberRange).send();
        assertNotNull(response.getResult());
    }
}
