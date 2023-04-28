from base.testing import KlaytnBaseTesting


class TestMyVotes(KlaytnBaseTesting):

    def test_post(self):
        governance_response = self.sdk.governance.my_votes()

        self.covert_response(governance_response.response)
        self.assertResponseSuccess()
        self.assertIn("result", self.response)
