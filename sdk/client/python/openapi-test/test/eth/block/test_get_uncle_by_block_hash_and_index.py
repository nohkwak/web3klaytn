from base.testing import KlaytnBaseTesting


class TestEthGetUncleByBlockHashAndIndex(KlaytnBaseTesting):

    def setUp(self) -> None:
        super().setUp()
        self.blockHash = "0xb8deae63002d2b6aa33247c8ef545383ee0fd2282ac9b49dbbb74114389ddb5c"
        self.uncleIndex = "0x1"

    def test_post(self):
        eth_response = self.sdk.eth.get_uncle_by_block_hash_and_index(
            self.blockHash, self.uncleIndex
        )

        self.covert_response(eth_response.response)
        self.assertResponseSuccess()
        self.assertIn("result", self.response)

    def test_post_wrong_with_lack_paramaters(self):
        eth_response = self.sdk.eth.get_uncle_by_block_hash_and_index(self.blockHash)

        self.covert_response(eth_response.response)
        self.assertResponseSuccess()
        self.assertIn("error", self.response)
        self.assertErrorCodeMissingRequiredArgument()
