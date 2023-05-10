from base.testing import KlaytnBaseTesting


class TestGetRawTransactionByBlockHashAndIndex(KlaytnBaseTesting):

    def setUp(self) -> None:
        super().setUp()
        self.blockHash = "0x4c4cbf242a80183d2ea2daf047c578d5fc89c0b14c4262606c8b6bb0b36715be"
        self.index = "0x0"

    def test_post(self):
        self.response = self.sdk.eth.get_raw_transaction_by_block_hash_and_index(
            self.blockHash, self.index
        )
        self.assertResponseSuccess()

    def test_post_wrong_with_lack_paramaters(self):
        self.response = self.sdk.eth.get_raw_transaction_by_block_hash_and_index()
        self.assertErrorCodeMissingRequiredArgument()
