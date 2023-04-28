from base.testing import KlaytnBaseTesting


class TestDebugGetModifiedAccountsByHash(KlaytnBaseTesting):

    def setUp(self) -> None:
        super().setUp()
        self.startBlockHash = "0xf07cd36ec44fc4b540dd9423317fd49171f03cc6063e8b517dfc9fe14d08ab7a"
        self.endBlockHash = "0xef15330537698b6cdfe31966cd0e0264af191c828a03a1a40e23ad465917b215"

    def test_post(self):
        debug_response = self.sdk.debug.get_modified_accounts_by_hash(
            self.startBlockHash, self.endBlockHash
        )

        self.covert_response(debug_response.response)
        self.assertResponseSuccess()
        self.assertIn("result", self.response)

    def test_post_wrong_with_lack_paramaters(self):
        debug_response = self.sdk.debug.get_modified_accounts_by_hash()

        self.covert_response(debug_response.response)
        self.assertResponseSuccess()
        self.assertIn("error", self.response)
        self.assertErrorCodeMissingRequiredArgument()
